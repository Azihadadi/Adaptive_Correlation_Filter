from __future__ import print_function
import cv2
from common.utils import RectSelector
from core.mosse import MOSSE

class Controller:
    def __init__(self, Root, video_src, paused=False):
        self.root = Root
        self.cap = self.capture(video_src)
        _, self.frame = self.cap.read()
        cv2.imshow('frame', self.frame)
        # get and draw the init ground truth (ROI)...
        self.rect_sel = RectSelector('frame', self.onrect)
        self.trackers = []
        self.paused = paused

    def onrect(self, rect):
        frame_gray = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)
        tracker = MOSSE(self.root, frame_gray, rect)
        self.trackers.append(tracker)

    def run(self):
        while True:
            if not self.paused:
                ret, self.frame = self.cap.read()
                if not ret:
                    break
                frame_gray = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)
                for tracker in self.trackers:
                    tracker.update(frame_gray, self.root.lr.get())

            vis = self.frame.copy()
            for tracker in self.trackers:
                tracker.draw_state(vis)
            if len(self.trackers) > 0:
                cv2.imshow('tracker', self.trackers[-1].state_vis)
            self.rect_sel.draw(vis)
            cv2.imshow('frame', vis)
            if (self.root.video_src != ''):
                ch = cv2.waitKey(70)
            else:
                ch = cv2.waitKey(10)
            if ch == 27:
                break
            if ch == ord(' '):
                self.paused = not self.paused
            if ch == ord('c'):
                self.trackers = []
        cv2.destroyAllWindows()

    def capture(self,source=0):
        source = str(source).strip()
        chunks = source.split(':')

        if len(chunks) > 1 and len(chunks[0]) == 1 and chunks[0].isalpha():
            chunks[1] = chunks[0] + ':' + chunks[1]
            del chunks[0]

        source = chunks[0]
        try:
            source = int(source)
        except ValueError:
            pass
        params = dict(s.split('=') for s in chunks[1:])

        cap = cv2.VideoCapture(source)
        if 'size' in params:
            w, h = map(int, params['size'].split('x'))
            cap.set(cv2.CAP_PROP_FRAME_WIDTH, w)
            cap.set(cv2.CAP_PROP_FRAME_HEIGHT, h)
        if cap is None or not cap.isOpened():
            print('Warning: unable to open video source: ', source)
        return cap


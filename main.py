import cv2 as cv
import datetime
import functions as func
video = cv.VideoCapture(0)
fps_start_time = datetime.datetime.now()
fps_number = 0
total_frames = 0
old_sudoku = None
while True:
    frame,success = func.read_video(video)
    total_frames = total_frames + 1
    fps_end_time = datetime.datetime.now()
    time_diff = fps_end_time - fps_start_time
    if time_diff.seconds == 0 :
        fps_number = 0,0
    else :
        fps_number = (total_frames/time_diff.seconds)
    if success :
        sudoku_game = func.recognize_and_solve_sudoku(frame,old_sudoku)
        cv.imshow("Reaal time sudoku solver.",sudoku_game)
        if cv.waitKey(1) & 0XFF == ord('q'):
            break
    else:
        break
video.release()
cv.destroyAllWindows()        
            
        

  



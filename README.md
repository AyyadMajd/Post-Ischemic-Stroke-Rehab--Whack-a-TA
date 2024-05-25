# Post-Ischemic-Stroke-Rehab--Whack-a-TA


Introduction:
Hello, welcome to our BE3100 EMG project slide cast! We are Group 12. Our group members are Majd
Ayyad, Shriya Boyapati, McKenzie Davis, and Sophie Gu. Today we will be talking about our final
project: Whack A TA, a physical-rehabilitation focused, interactive game.


Objectives:
The objective of this project is guided by the physiological mechanism of ischemic stroke, which
generally occurs when a blood clot blocks or plugs an artery leading to the brain. Ischemic stroke often
results in motor cortex and corticospinal weakness, thus contributing to muscle impairments and fatigue.
Leveraging this pathophysiology, we developed the concept for our final project: a whack-a-mole like
game that allows users to rehabilitate from stroke using isometric exercise. In this game, users are tasked
with flexing their muscles in order to “hit” the TAs incorporated in the project.
Design Overview:

The game itself is split into 4 main components. Firstly, the device is calibrated, allowing a EMG signal
threshold to be determined for each user. The threshold is stored and utilized in order to determine
whether a user was successful in meeting the requirements of the game. In particular, a user may be
prompted to hold a flex for 6 seconds or 3 seconds – the threshold is used to determine if these conditions
are met and then directs the servo to hit the appropriate TA with either a CW or CCW turn. A point is
earned for each hit. When the user completes 3 successful flexes, the game is completed and the user
wins. The game parameters are easily adjustable, allowing physical therapists and healthcare providers to
alter the task difficulty required to hit a “TA,” or the number of successful flexes required to complete the
game, depending on a patients’ stage of recovery.

EMG Signal:
In order to obtain usable EMG data, the raw EMG required both physical and digital filtering. First, the
EMG signal was passed through various hardware elements, including high pass and bandpass filters,
buffer stage, differential amplifier, non-inverting amplifier, and a full wave rectifier. Then, the signal was
processed digitally via a moving average digital filter in order to calculate a threshold EMG value per
user. The user was prompted to flex hard for four seconds during the calibration stage. The maximum
amplitude of the filtered signal was recorded for each second and then averaged among the four second
periods. The threshold was defined to be 60% of the result (mean value of maximum amplitudes). The
percentage choice was made to account for the viability of the strength of flexing (users may not flex as
hard while being distracted by the game). We would like to note that the data was collected in points
rather than seconds. Essentially, we programmed the Arduino to output data at a rate of 1000 Hz (or
roughly .05 points per seconds).


Design:
This is a picture of the CAD enclosure for the game, designed to fit the springs required for the TA figures
(1). These are the different screens in our GUI. The first screen is the Whack A Ta starting screen. Once
the user clicks Start, they should select the connect BLE button and click calibrate. The user will be
notified via text when calibration is complete and they can then click begin the game. When three points
are achieved, a text that congratulates the user appears (2).
Results:
(1 min) This video showcases one representative demo of the game. In this video, the user begins the
game by clicking START. Then, the user selects connect BLE, calibrates the device by flexing for four
seconds and clicks begin game. Here, we see the user is prompted to flex 6 seconds in order to hit the TA.
After successfully doing so, the point counter increases to 1, and the servo motor moves to hit the TA.
Then the user is prompted to flex 3 seconds to hit the other TA and once more for 6 seconds, ultimately
leading to the victory screen. (1)

Our results were validated via meticulous testing of the game design. 10 users were required to play the
game as expected 3x each. These were considered “true” positive trials. They were also tasked with not
flexing at all during the duration of the game 1x each. These were considered no flex trials. More
specifically, a true positive trial occurs when the user flexes and the score increases by 1 and the servo
motor moves to hit the correct target. No flex is indicated by no increase in score and no/incorrect servo
motor movement (also detonated as a false positive). (2)
We found that true flex trials were accomplished 29/30 times, or a 96.7% success rate. Our data was
associated with a standard deviation of 2%. Although overall promising results, we aim to increase our
success rate by incorporating more rigorous thresholding and digital data processing. No flex trials
succeeded 100% of the time, indicating that the calibration process successfully identified proper
thresholds per user and a false positive rate of 0%. (3)
(22 seconds) This video shows a “no flex” trial, where the user did not flex when prompted to do so and
the point value remained the same and the motor did not move as expected.


Discussion:
Overall, the game was relatively consistent in its performance across trials. In order to better the user
experience, we aim to test methods to increase bluetooth connection reliability and coordinate
circuitry/wiring so any loose connections can be easily identified and fixed. Additionally, testing different
numbers of points taken for the moving average may increase flex detection capabilities in the device.
In terms of major challenges, we struggled with servo motor jitter. Although we utilized different python
libraries and code AND reset the raspberry pi SD card, we were unable to reduce the jitter. We hope to
address the issue in the future by looking into additional libraries and motors that can handle the tasks in
the algorithm.

Conclusion:
Equipped with the learnings from this design process, we hope to produce more refined iterations by
adding additional “moles” or motors to increase game complexity, adjusting the GUI to reflect different
levels, and modifying the game to account for differences in muscle groups.
Acknowledgements:
We would like to note that all group members contributed equally to the development of this slidecast. A
final thank you to the teaching staff for their help throughout the year – you are invaluable mentors and an
inspiration for us all :)

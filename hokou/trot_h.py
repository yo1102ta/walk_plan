import Adafruit_PCA9685
import time

class servo:
    PULSE_MIN = 100
    PULSE_MAX = 510
    MAX_ANGLE = 180
    def __init__(self, Channel):
        self.Channel = Channel
        self.pwm = Adafruit_PCA9685.PCA9685(0x40)
        self.pwm.set_pwm_freq(50)

    def setPos(self,pos):

        pulse = int((self.PULSE_MAX - self.PULSE_MIN) / self.MAX_ANGLE * pos + self.PULSE_MIN)
        self.pwm.set_pwm(self.Channel, 0, pulse)

pos = 0
s0 = servo(0)
s1 = servo(1)
s2 = servo(2)
s4 = servo(4)
s5 = servo(5)
s6 = servo(6)
s8 = servo(8)
s9 = servo(9)
s10 = servo(10)
s12 = servo(12)
s13 = servo(13)
s14 = servo(14)

#katamuki
k=2
k2=2

s0_f=100
s1_f=119
s2_f=115

s4_f=80
s5_f=80
s6_f=65

s8_f=80
s9_f=123+k
s10_f=133-k2

s12_f=70
s13_f=84-k
s14_f=71+k2

s=[s0_f,s1_f,s2_f,0,s4_f,s5_f,s6_f,0,s8_f,s9_f,s10_f,0,s12_f,s13_f,s14_f]

motion1=[[-42, 66], [-47, 72], [-49, 78], [-49, 81], [-47, 81], [-46, 82], [-44, 82], [-43, 82], [-39, 79], [-35, 74], [-33, 67], [-34, 65]]
#0-11
motion2=[[-35, 65], [-37, 65], [-38, 64], [-39, 64]]#0-3

#set
#time.sleep(3)
s[1]=-motion2[7][0]+s1_f
s[2]=-motion2[7][1]+s2_f

s[5]=motion1[15][0]+s5_f
s[6]=motion1[15][1]+s6_f

s[9]=-motion1[15][0]+s9_f
s[10]=-motion1[15][1]+s10_f

s[13]=motion2[7][0]+s13_f
s[14]=motion2[7][1]+s14_f

s0.setPos(s[0])
s4.setPos(s[4])
s8.setPos(s[8])
s12.setPos(s[12])
#time.sleep(0.5)
s1.setPos(s[1])
s2.setPos(s[2])
s9.setPos(s[9])
s10.setPos(s[10])
#time.sleep(0.5)
s5.setPos(s[5])
s6.setPos(s[6])
s13.setPos(s[13])
s14.setPos(s[14])
time.sleep(2)

i=0
j=0
t1 = time.time()
while True:
	print ("i:"+str(i))
	print ("j:"+str(j))
	if i<=11:
		s[1]=-motion1[i][0]+s1_f
		s[2]=-motion1[i][1]+s2_f
		s[13]=motion1[i][0]+s13_f
		s[14]=motion1[i][1]+s14_f
		s[5]=motion2[j][0]+s5_f
		s[6]=motion2[j][1]+s6_f
		s[9]=-motion2[j][0]+s9_f
		s[10]=-motion2[j][1]+s10_f


	elif i>=12:
		s[9]=-motion1[i-12][0]+s9_f
		s[10]=-motion1[i-12][1]+s10_f
		s[5]=motion1[i-12][0]+s5_f
		s[6]=motion1[i-12][1]+s6_f
		s[13]=motion2[j][0]+s13_f
		s[14]=motion2[j][1]+s14_f
		s[1]=-motion2[j][0]+s1_f
		s[2]=-motion2[j][1]+s2_f

	s0.setPos(s[0])
	s1.setPos(s[1])
	s2.setPos(s[2])
	s4.setPos(s[4])
	s5.setPos(s[5])
	s6.setPos(s[6])
	s8.setPos(s[8])
	s9.setPos(s[9])
	s10.setPos(s[10])
	s12.setPos(s[12])
	s13.setPos(s[13])
	s14.setPos(s[14])

	#time.sleep(0.001)
	i+=1
	if i%3==0 :
			j+=1

	if i==12 or i==24:
		time.sleep(0.01)
		j=0

	if i==24:
		t2 = time.time()
		i=0
		j=0
		print(t2-t1)
		t1 = time.time()

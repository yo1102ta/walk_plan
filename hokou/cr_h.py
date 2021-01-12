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
ka=0
ka2=2
s0_f=100+ka2
s1_f=119
s2_f=115

s4_f=80+ka2
s5_f=80+ka
s6_f=65

s8_f=80+ka2
s9_f=123-ka
s10_f=133

s12_f=70+ka2
s13_f=84
s14_f=71

s=[s0_f,s1_f,s2_f,0,s4_f,s5_f,s6_f,0,s8_f,s9_f,s10_f,0,s12_f,s13_f,s14_f]

#motion1=[[-42, 66], [-47, 72], [-49, 78], [-49, 81], [-47, 81], [-46, 82], [-44, 82], [-43, 82], [-39, 79], [-35, 74], [-33, 67], [-34, 65],
#[-35, 65], [-37, 65], [-38, 64], [-39, 64]]
#-30
#motion1=[[-45, 64], [-49, 70], [-52, 76], [-52, 80], [-50, 80], [-49, 81], [-47, 81], [-46, 82], [-42, 80], [-38, 74], [-36, 67], [-37, 65],
#[-38, 64], [-38, 64], [-39, 64], [-40, 63], [-40, 63], [-41, 62]]
#-40
#motion1=[[-46, 62], [-51, 68], [-54, 74], [-54, 78], [-53, 79], [-52, 80], [-50, 80], [-49, 81], [-46, 79], [-41, 74], [-39, 67], [-39, 64],
# [-40, 63], [-40, 63], [-41, 62], [-42, 62], [-42, 62],[-43, 61]]
#-60
motion1=[[-49, 56], [-53, 62], [-57, 69], [-58, 74], [-57, 75], [-56, 76], [-55, 77], [-54, 78], [-51, 77], [-47, 72], [-44, 65], [-43, 61],
[-44, 60],[-44, 60], [-45, 58], [-46, 57],  [-46, 57], [-46, 55]]


#20
motion2=[[-31, 67], [-35, 74], [-37, 79], [-36, 81], [-34, 80], [-32, 80], [-30, 79], [-28, 78], [-24, 74], [-20, 68], [-18, 62], [-20, 61],
[-22, 62], [-22, 62], [-24, 62], [-25, 63], [-25, 63], [-27, 64]]


#set

time.sleep(3)
s[1]=-motion1[11][0]+s1_f
s[2]=-motion1[11][1]+s2_f
s[5]=motion1[15][0]+s5_f
s[6]=motion1[15][1]+s6_f
s[9]=-motion2[11][0]+s9_f
s[10]=-motion2[11][1]+s10_f
s[13]=motion2[15][0]+s13_f
s[14]=motion2[15][1]+s14_f


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
#katamuki
k=10
#5
#8
#15
k2=6
b=1
count_ave=0
cy_ave=0
t1 = time.time()
while True:
	#print("i="+str(i))
	#print("j="+str(j))
	if j<=11:
		s[5]=motion1[i][0]+s5_f
		s[6]=motion1[i][1]+s6_f

		s[0]=s0_f+k
		s[8]=s8_f+k
		s[4]=s4_f+k
		s[12]=s12_f+k


	elif 12<=j and j<=23:
		s[13]=motion2[i][0]+s13_f
		s[14]=motion2[i][1]+s14_f

		s[0]=s0_f+k
		s[8]=s8_f+k
		s[4]=s4_f+k
		s[12]=s12_f+k

	elif 24<=j and j<=26:
		s[1]=-motion1[i+14][0]+s1_f
		s[2]=-motion1[i+14][1]+s2_f
		s[5]=motion1[i+12][0]+s5_f
		s[6]=motion1[i+12][1]+s6_f
		s[9]=-motion2[i+14][0]+s9_f
		s[10]=-motion2[i+14][1]+s10_f
		s[13]=motion2[i+12][0]+s13_f
		s[14]=motion2[i+12][1]+s14_f

		s[4]=s4_f
		s[12]=s12_f
		s[8]=s8_f
		s[0]=s0_f

		if j==25:
			s[0]=s0_f-k2
			s[8]=s8_f-k2
			s[4]=s4_f-k2
			s[12]=s12_f-k2

	elif 27<=j and j<=38:
		s[1]=-motion1[i][0]+s1_f
		s[2]=-motion1[i][1]+s2_f

		s[4]=s4_f-k
		s[12]=s12_f-k
		s[0]=s0_f-k
		s[8]=s8_f-k

	elif 39<=j and j<=50:
		s[9]=-motion2[i][0]+s9_f
		s[10]=-motion2[i][1]+s10_f

		s[4]=s4_f-k
		s[12]=s12_f-k
		s[8]=s8_f-k
		s[0]=s0_f-k

	elif 51<=j and j<=53:
		s[1]=-motion1[i+12][0]+s1_f
		s[2]=-motion1[i+12][1]+s2_f
		s[5]=motion1[i+14][0]+s5_f
		s[6]=motion1[i+14][1]+s6_f
		s[13]=motion2[i+14][0]+s13_f
		s[14]=motion2[i+14][1]+s14_f
		s[9]=-motion2[i+12][0]+s9_f
		s[10]=-motion2[i+12][1]+s10_f

		s[0]=s0_f
		s[8]=s8_f
		s[4]=s4_f
		s[12]=s12_f

		if j==52:
			s[0]=s0_f+k2
			s[8]=s8_f+k2
			s[4]=s4_f+k2
			s[12]=s12_f+k2

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

	time.sleep(0.01)
	#s[5] = int(input()) #iを取得し、intに値を入れる

	#print(s[1]-s1_f)

	i+=1
	j+=1

	if j==12 or j==24 or j==27 or j==39 or j==51 or j==54:
		i=0
		time.sleep(0.05)


	if j==54:
		i=0
		j=0
		count_ave+=1
		t2 = time.time()
		cy=t2-t1
		print(cy)
		cy_ave+=cy

		if count_ave%10==0 :
			print ("\nAve:"+str(cy_ave)+"\n")
			cy_ave=0
		t1 = time.time()

	#if j==52:
	#	i=0
	#	j=0

	#time.sleep(0.5)

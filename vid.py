import cv2
imgs = []

total_length = 300
curr_length = 0

frame_rate = 8
sec_per_frame = 1/frame_rate

# 2:12~2:43  31 sec

for i in range(3928, 4030):
#for i in range(4464, 4595):
	imgs.append(cv2.imread('images\DSC_%d.JPG' % i))
	if i % 10 == 0: print('\r%d' % i, end='')
else: print()

#fourcc = cv2.VideoWriter_fourcc(*'XVID')
fourcc = cv2.VideoWriter_fourcc(*'WMV1')
#out = cv2.VideoWriter('output5_full.avi',fourcc, 10., (4928,3264))
out = cv2.VideoWriter('output\FA2_1.wmv',fourcc, frame_rate, (4928,3264))
out.write(imgs[0])

for i in range(4):
	print('Loop %d' % i)
	for j, im in enumerate(imgs):
		#if j == 50: break
		if j % 10 == 0:
			print('\r\t%d' % j, end='')
		if j == len(imgs)-1: break
		for k in range(1, 13):
			img_mix = cv2.addWeighted(imgs[j], 0.2/3 * (13-k), imgs[j+1], 0.2/3*k, 0)
			out.write(img_mix)
			curr_length += sec_per_frame
			if curr_length > total_length: break
		if curr_length > total_length: break
	print()
	if curr_length > total_length: break
	
out.release()
		
			
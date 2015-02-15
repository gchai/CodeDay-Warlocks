# ColorMod will take in pygame images as arguments, and return images back.
#
#
#
#
#
#
#
import pygame
from pygame.locals import *
pygame.init()
def GetLumin(imgparam):
	'''returns an image in black and white.'''
	img = imgparam.copy()
	w = 0
	h = 0
	while w < img.get_width():
		while h < img.get_height():
			pix = img.get_at((w,h))
			R = pix[0]
			G = pix[1]
			B = pix[2]
			A = pix[3]
			Y = 0.2126*R + 0.7152*G + 0.0722*B
			img.set_at((w,h), (Y,Y,Y,A))
			h += 1
		h= 0
		w+=1
	return img
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`
def Filter(imgparam, color = (255,0,0), mid = 255):
	'''returns an image filtered so that (mid,mid,mid) becomes the color given.'''
	img = imgparam.copy()
	w = 0
	h = 0
	while w < img.get_width():
		while h < img.get_height():
			pix = img.get_at((w,h))
			r = pix[0]
			g = pix[1]
			b = pix[2]
			A = pix[3]
			r = r * color[0]/mid
			if r > 255:
				r = 255
			elif r <0:
				r = 0
			g = g * color[1]/mid
			if g > 255:
				g = 255
			elif g <0:
				g = 0
			b = b * color[2]/mid
			if b > 255:
				b = 255
			elif b <0:
				b = 0
			img.set_at((w,h), (r,g,b,A))
			h += 1
		h= 0
		w+=1
	return img
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`
def Colorize(imgparam, color = (255,0,120), mid = 126):
	img = GetLumin(imgparam)
	img = Filter(img, color, mid)
	return img
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`
def Transparency(imgparam, value = 0):
	img = imgparam.copy()
	w = 0
	h = 0
	if value <= 0:
		value = 2
	while w < img.get_width():
		while h < img.get_height():
			pix = img.get_at((w,h))
			r = pix[0]
			g = pix[1]
			b = pix[2]
			a = pix[3]
			if a == 0:
				img.set_at((w,h), (r,g,b,a))
			else:
				img.set_at((w,h), (r,g,b,value))
			h += 1
		h= 0
		w+=1
	return img
def Inverse(imgparam):
	img = imgparam.copy()
	w = 0
	h = 0
	while w < img.get_width():
		while h < img.get_height():
			R = 255- img.get_at((w,h))[0]
			G = 255- img.get_at((w,h))[1]
			B = 255- img.get_at((w,h))[2]
			A = img.get_at((w,h))[3]
			img.set_at((w,h), (R,G,B,A))
			h += 1
		h= 0
		w+=1
	return img

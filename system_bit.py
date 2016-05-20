#!/usr/bin/env python
# -*- coding: utf-8 -*-

import platform

def system_name_and_bit_info():
	info_ico = """
			  GH0ST-S0FTWARE
	# ------------------------------------------------#
	# - Işletim Sistemi 	|         Çıktı          -#
	# ------------------------------------------------#
	# -  32 bit Linux 	| ('32bit', 'ELF')       -#
	# -  64 bit Linux 	| ('64bit', 'ELF')       -#
	# - 32 bit Windows 	| ('32bit', 'WindowsPE') -#
	# - 64 bit Windows 	| ('64bit', 'WindowsPE') -#
	# ------------------------------------------------#
	"""
	print info_ico
	print "İşletim sisiteminiz : ", platform.architecture()

system_name_and_bit_info()

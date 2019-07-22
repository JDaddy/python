#!/usr/bin/env python3

import shutil
import os
# This allows convenience of changing directories
os.chdir('/home/student/python/')
# This allows you to copy a file from one path to another
shutil.copy('5g_research/sdn_network.txt', '5g_research/sdn_network.txt.copy')
# This will copy an entire folder and return the copied folder path
shutil.copytree('5g_research/', '5g_research_backup/')



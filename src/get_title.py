# -*- coding: utf-8 -*-
import win32gui

output = []

def callback(hwnd, strings):
    if win32gui.IsWindowVisible(hwnd):
        window_title = win32gui.GetWindowText(hwnd)
        left, top, right, bottom = win32gui.GetWindowRect(hwnd)
        if window_title and right-left and bottom-top:
            strings.append('0x{:08x}: "{}"'.format(hwnd, window_title))
    return True

def get_title():
    win_list = []  # list of strings containing win handles and window titles
    win32gui.EnumWindows(callback, win_list)  # populate list

    for window in win_list:  # print results
        output.append(window)
    
    return output
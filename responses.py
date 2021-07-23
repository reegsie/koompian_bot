
from datetime import datetime
from long_str import *

def main_listener(input_text):
    
    # Taking user input
    user_message = str(input_text).lower()
    
    # How
    if "how" in user_message:
        if "update" in user_message:
            if "zoom" in user_message:
                return update_zoom
        if "download" in user_message:
            if "photoshop" in user_message:
                return photoshop
            if "devc++" in user_message:
                return devc
            if "video" in user_message:
                return download_video
            if "discord" in user_message:
                return download_discord
            if "update" in user_message:
                return system_update
            if "zoom" in user_message:
                return zoom_install
        if "change" in user_message:
            if "wallpaper" in user_message:
                return change_wall
            if "wall paper" in user_message:
                return change_wall
    # Zoom
    if "zoom" in user_message:
        if "can't" in  user_message:
            if "launch" in user_message:
                return zoom_fault_launch
            if "open" in user_message:
                return zoom_fault_launch
        if "not" in user_message:
            if "opening" in user_message:
                return zoom_fault_launch
            
    # problemI tried to turn it off but it doesn't work n
    if "problem" in user_message:
        if "screen" in user_message:
            return location
        if "keyboard" in user_message:
            return location
        if "battery" in user_message:
            return location
        if "laptop" in user_message:
            return location
        if "touchpad" in user_message:
            return location
        if "speaker" in user_message:
            return location
        if "camera" in user_message:
            return location
    if "problems" in user_message:
        if "office" in user_message:
            return location
        if "place" in user_message: 
            return location
        if "send" in user_message:
            if "office" in user_message:
                return location
            if "place" in user_message:
                return location
    #tried
    if "tried" in user_message:
        if "turn" in user_message:
            if "off" in user_message:
                return power_off
            
    # អត់
    if "អត់" in user_message:
        if "ចេញអក្សរចិនបង" in user_message:
            return chinese_not_working
        
    # sing in problem   
    if "cannot" in user_message:
        if "sign" in user_message:
            if "account" in user_message:
                return 
            
    # General Questoin
    if "can" in user_message: 
        if "use" in user_message:
            if "sudo apt" in user_message:
                return pacman
        if "stream" in user_message:
            if "iphone" in user_message:
                if "obs" in user_message:
                    return ndi
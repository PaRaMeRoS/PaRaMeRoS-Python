#Copyright (c) 2024 Maximilian Gründinger

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.

# import Area
import time
import logging
import os
import sys

print("Python is starting...")

# Konfigurieren des Loggers
logger = logging.getLogger('backend_new.py')
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler('./backend.log')
fh.setLevel(logging.DEBUG)
logger.addHandler(fh)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)

# var Area Placeholder till config
file_input = "(system)"
running = True
User = "Team"
dir0 = "/home/web/website/PaRaMeRoS-Python/directory.fll"
in0 = "/home/web/website/PaRaMeRoS-Python/output.fll"
out0 = "/home/web/website/PaRaMeRoS-Python/input.fll" 
start0 = "/home/web/website/PaRaMeRoS-Python/start.fll"
user0 = "/home/web/website/PaRaMeRoS-Python/user.fll"
config0 = "/home/web/website/PaRaMeRoS-Python/config.fll"
real_admin_user = ["ZRHztr65"]
admin_user = ["David", "Max"]
normal_user = ["Team", "Coach!"]
index = None
user_input = None
permision_input = None
time_wait = int(2)

#Listen von den DIR´s
DIR_LIST = ['terminal', 'terminal-en', 'terminal-en-conf', 'terminal-en-conf-sys', 'terminal-en-conf-sys-spi']
#Listen von Weiterführung zu DIR
WEITERDIR_LIST = ['end', 'exit', 'en', 'do', 'show', 'conf -t', 'sys -conf', 'conf -spi', ]
#Alle Befehle
ALL_LIST = ['en', 'conf -t', 'conf -sys', 'conf -spi', 'end', 'exit', 'help', 'update', 'do shutdown', 'do bootup', 'do reboot', 'show files', 'show conf', 'show status', "upload '{file_input}'", "download '{file_input}'", "remove", 'spike charge', 'change permision', "exit_script", "pwd", "grep file", "command"]
#valid combinations
VALIDS = [(0, 0), (1, 1), (2, 2), (3, 3), (0, 4), (1, 4), (2, 4), (3, 4), (4, 4), (1, 5), (2, 5), (3, 5), (4, 5), (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (3, 8), (4, 8), (3, 9), (3, 10), (2, 11), (3, 11), (4, 11), (2, 12), (2, 13), (3, 13), (4, 13), (3, 14), (3, 15), (4, 15), (3, 16), (4, 17), (3, 18), (0,20), (1,20), (2,20), (3,20), (4,20), (2,21),(3,22)]
#valid combinations with user
ADMIN_VALIDS = [(0, 0), (1, 1), (2, 2), (3, 3), (0, 4), (1, 4), (2, 4), (3, 4), (4, 4), (1, 5), (2, 5), (3, 5), (4, 5), (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (3, 8), (4, 8), (3, 9), (3, 10), (2, 11), (3, 11), (4, 11), (2, 12), (2, 13), (3, 13), (4, 13), (3, 14), (3, 15), (4, 15), (3, 16), (4, 17)]



# Funktionen
OUT_LIST = {
    (0, 0): "terminal-en",
    (1, 1): "terminal-en-conf",
    (2, 2): "terminal-en-conf-sys",
    (3, 3): "terminal-en-conf-sys-spi",
    (0, 4): "terminal",
    (1, 4): "terminal",
    (2, 4): "terminal",
    (3, 4): "terminal",
    (4, 4): "terminal",
    (1, 5): '',
    (2, 5): '',
    (3, 5): '',
    (4, 5): '',
    (0, 6): f"en&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;Enables&nbsp;the&nbsp;system&nbsp;configuration&nbsp;mode\n&nbsp;some&nbsp;comands&nbsp;like&nbsp;delet&nbsp;file&nbsp;takes&nbsp;extra&nbsp;Argument&nbsp;with&nbsp;an&nbsp;,&nbsp;&nbsp;lease&nbsp;try&nbsp;to&nbsp;care&nbsp;for&nbsp;under&nbsp;scores",
    (1, 6): f"exit&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;goes&nbsp;to&nbsp;terminal</br>\nend&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;goes&nbsp;to&nbsp;terminal</br>\nupdate&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;updates&nbsp;the&nbsp;Conntent</br>\nshow&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;goes&nbsp;to&nbsp;dir&nbsp;show&nbsp;(files/shows&nbsp;files,&nbsp;status/shows&nbsp;status)</br>\nconf&nbsp;-t/configure&nbsp;terminal&nbsp;&nbsp;-&nbsp;goes to terminal-en-conf</br>",
    (2, 6): f"exit&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;goes&nbsp;to&nbsp;terminal</br>\nend&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;goes&nbsp;to&nbsp;terminal</br>\nupdate&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;updates&nbsp;the&nbsp;Conntent</br>\ndo&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;goes&nbsp;to&nbsp;dir&nbsp;do&nbsp;(shutdown/shutssdown&nbsp;the&nbsp;system,&nbsp;bootup/bootsup&nbsp;the&nbsp;system,&nbsp;reboot/reboots&nbsp;the&nbsp;system)</br>\nsys&nbsp;-conf&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;goes&nbsp;to&nbsp;terminal-#-conf-sys</br>",
    (3, 6): f"exit&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;goes&nbsp;to&nbsp;terminal</br>\nend&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;goes&nbsp;to&nbsp;terminal</br>\nupdate&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;updates&nbsp;the&nbsp;Conntent</br>\ndo&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;goes&nbsp;to&nbsp;dir&nbsp;do&nbsp;(shutdown/shutssdown&nbsp;the&nbsp;system,&nbsp;bootup/bootsup&nbsp;the&nbsp;system,&nbsp;reboot/reboots&nbsp;the&nbsp;system)</br>\n<span class='color2'>upload&nbsp;file&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;uploads&nbsp;an&nbsp;file&nbsp;to&nbsp;the&nbsp;server</span></br>\n<span class='color2'>download&nbsp;file&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;downloads&nbsp;an&nbsp;file&nbsp;from&nbsp;the&nbsp;server</span></br>\n<span class='color2'>remove&nbsp;file&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;removes&nbsp;an&nbsp;file&nbsp;from&nbsp;the&nbsp;server,&nbsp;please&nbsp;enter&nbsp;file&nbsp;DIR</span></br>\n<span class='color2'>config&nbsp;file&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;configures&nbsp;an&nbsp;file&nbsp;from&nbsp;the&nbsp;server</span></br>\ncommand&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;admins&nbsp;can&nbsp;enter&nbsp;linux&nbsp;command</br>",
    (4, 6): f"exit&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;goes&nbsp;to&nbsp;terminal</br>\nend&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;goes&nbsp;to&nbsp;terminal</br>\nupdate&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;updates&nbsp;the&nbsp;Conntent</br>\nshow&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;goes&nbsp;to&nbsp;dir&nbsp;show&nbsp;(files/shows&nbsp;files,&nbsp;status/shows&nbsp;status)</br>\nspike&nbsp;charge&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;shows&nbsp;spike&nbsp;charge</br>",
    (0, 7): "Updating...",
    (1, 7): "Updating...",
    (2, 7): "Updating...",
    (3, 7): "Updating...",
    (4, 7): "Updating...",
    (3, 8): "",
    (4, 8): "",
    (3, 9): "",
    (3, 10): "Rebooting...",
    (2, 12): f"Configuration:\n{config0}",
    (2, 13): "Status:&nbsp;No&nbsp;Problems&nbsp;recorded",
    (3, 13): "Status:&nbsp;Online&nbsp;and&nbsp;running",
    (4, 13): "Status:&nbsp;Online",
    (3, 14): "Drag&nbsp;your&nbsp;file&nbsp;into&nbsp;the&nbsp;commandline!",
    (3, 15): "The&nbsp;file&nbsp;downloads&nbsp;into&nbsp;your&nbsp;Download&nbsp;folder!",
    (4, 15): "The&nbsp;file&nbsp;will&nbsp;download&nbsp;in&nbsp;a&nbsp;few&nbsp;seconds",
    (3, 16): "The&nbsp;file&nbsp;is&nbsp;getting&nbsp;removed&nbsp;please&nbsp;stand&nbsp;by!",
    (4, 17): "Spike&nbsp;Charging",
    (3, 18): "change&nbsp;user&nbsp;permission",
    (0, 19): "exiting&nbsp;the&nbsp;Skript...",
    (0, 20): "terminal",
    (1, 20): "terminal-en",
    (2, 20): "terminal-en-conf",
    (3, 20): "terminal-en-conf-sys",
    (4, 20): "terminal-en-conf-sys-spi",
    (2, 21): f"loading...\n"
}

class User:
    def __init__(self):
        # alle Dateien werden gelesen und aufbereitet für die Verarbeitung durch die Funktion command
        with open(user0, "r") as file:
            User = file.read().strip()

        with open(dir0, "r") as file:
            dir1 = file.read().strip()

        if not any(element in dir1 for element in DIR_LIST):
            with open(out0, "w") as f:
                input1 = f.read().strip()

        with open(in0, "r") as file:
            input234 = file.read().strip()
            input1 = input234
            user_input = None
        
        try: 
            input234 = input234.split(", ")
            user_input = input234[1]
            imput1 = input234[0]
            input1 = input1.replace(", ", "")

        except IndexError:
            imput1 = input234
            user_input = None
        
        if not any(element in input1 for element in ALL_LIST):
            null = None 

        index = None

        for j, element in enumerate(DIR_LIST):
            if element == dir1:
                index = j

        index1 = None

        for i, element in enumerate(ALL_LIST):
            if element == input1:
                index1 = i
            
        together = (index, index1)
        print(together)

        self.command(together, out0, index, User, user_input) # runn's the main logik
        
    def command(self, combination, file, index, User, variable_input=None):
        if combination == (1,5) or combination == (2,5) or combination == (3,5) or combination == (4,5):
            index -= 1
            self.write_file(dir0,DIR_LIST[index])
        elif combination == (0,19):
            self.write_file(in0, "exit")
            running = False
        elif combination == (4,22):
            self.command_os(variable_input)
        elif combination == (3,16):
            self.file_remove(variable_input)
            self.write_file(start0, "Done!")
        elif combination == (2,21):
            self.load_file_inhalt(variable_input)
            self.write_file(start0, "Done!")
        elif combination == (3,10):
            if check_user_admin(User):
                self.write_file(start0, "Done!")
                self.reboot(User)
            else:
                logger.debug("invalid_permision")
        elif combination == (3,9):
            if self.check_user_admin1(User):
                self.write_file(start0, "Done!")
                self.hard_shutdown(User)
            else:
                logger.debug("invalid_command")
        elif combination == (3,18):
            if check_user_admin1(User):
                usre = variable_input.split("-> ")
                user_input = usre[0]
                permision_input = usre[1]
                user_input = user_input.replace("-> ", "")
                self.change_user_permision(user_input, permision_input)
                self.write_file(start0, "Done!")
            else:
                logger.debug("invalid_permision")
                self.write_file(start0, "Done!")
        elif combination == (2,13):
            if self.check_user_admin(User):
                with open("backend.log", "r") as f:
                    self.write_file(out0, f.read())
                    self.write_file(start0, "Done!")
            else:
                logger.debug("invalid_permision")
        elif combination == (0,0) or combination == (1,1) or combination == (2,2) or combination == (3,3) or combination == (0,4) or combination == (1,4) or combination == (2,4) or combination == (3,4) or combination == (4,4):
            self.write_file(dir0, OUT_LIST[combination])
            self.write_file(out0, OUT_LIST[combination])
            self.write_file(start0, "Done!")
        elif combination == (0,6) or combination == (1,6) or combination == (2,6) or combination == (3,6) or combination == (4,6) or combination == (0,7) or combination == (1,7) or combination == (2,7) or combination == (3,7) or combination == (4,7) or combination == (3,8) or combination == (4,8) or combination == (3,9) or combination == (3,10) or combination == (2,11) or combination == (3,11) or combination == (4,11) or combination == (2,12) or combination == (2,13) or combination == (3,13) or combination == (4,13) or combination == (3,14) or combination == (3,15) or combination == (4,15) or combination == (3,16) or combination == (4,17) or combination == (0,20) or combination == (1,20) or combination == (2,20) or combination == (3,20) or combination == (4,20):
            self.write_file(file, OUT_LIST[combination])
            self.write_file(start0, "Done!")
        else:
            logger.debug("invalid_command")
            self.write_file(out0, "invalid command")

    def file_remove(self, file):
        if check_user_admin(User):
            logger.debug("file_remove_valid")
            os.remove(file)

    def command_os(self, command):
        if "sudo" in command: # disables sudo for normal user
            if check_user_admin1(User):
                com = os.system(command)
                with open(out0, "w") as f:
                    f.write(com)
                with open(start0, "w") as f:
                    f.write("Done!")
            with open(out0, "w") as f:
                f.write("invalid command")
            with open(start0, "w") as f:
                f.write("Done!")
        else:
            com = os.system(command)
            with open(out0, "w") as f:
                f.write(com)
            with open(start0, "w") as f:
                f.write("Done!")

    def load_file_inhalt(self, file):
        if check_user_admin(User):
            logger.debug("load_file_inhalt_valid")
            with open(file, "r") as f:
                self.write_file(out0, f.read())
        else:
            logger.debug("load_file_inhalt_invalid")

    def file_removefile_path(self, file_path):
        if check_user_admin1(User):
            logger.debug("file_remove_valid")
            os.remove(file_path)

    def check_user_admin(self, current_user):
        if current_user in admin_user:
            logger.debug("check_user_valid")
            return True
        elif current_user in real_admin_user:
            logger.debug("check_user_valid")
            return True
        else:
            logger.debug("check_user_invalid")
            return False

    def check_user_admin1(self, current_user):
        if current_user in admin_user:
            logger.debug("check_user_valid")
            return False
        elif current_user in real_admin_user:
            logger.debug("check_user_valid")
            return True
        else:
            logger.debug("check_user_invalid")
            return False

    def hard_shutdown(self, User):
        if check_user_admin(User):
            logger.debug("hard_shutdown_valid")
            os.system("reboot -f")

    def reboot(self, User):
        if check_user_admin(User):
            logger.debug("reboot_valid")
            os.system("reboot")

    def write_file(self, file, text):
        with open(file, "w") as f:
            f.write(text)
        with open(start0, "w") as f:
            f.write("Done!")

    def change_user_permision(self, user, permision):
        if self.check_user_admin(User):
            logger.debug("change_user_permision_valid")
            if permision == "admin":
                logger.debug("change_user_permision_valid")
                admin_user.append(user)
                normal_user.remove(user)
            elif permision == "normal":
                logger.debug("change_user_permision_valid")
                normal_user.append(user)
                admin_user.remove(user)
            else:
                logger.debug("change_user_permision_invalid")


class config:
    # Hier Config auslese und conf einbauen
    def __init__(self):
        with open("config.config", "r") as f: #/home/web/website/PaRaMeRoS-Python/
            lines = f.readlines()
            read = lines[0].split(", ")
            read[0] = read[0].replace(", ", "")
            read[0] = str(out0)
            read[1] = read[1].replace(", ", "")
            in0 = str(read[1])
            dir0 = str(read[2])
            start0 = str(read[3])
            user0 = str(read[4])
            admin_user = []
            real_admin_user = []
            normal_user = []
            admin_user.append(str(lines[1].strip()))
            real_admin_user.append(str(lines[2].strip()))
            normal_user.append(str(lines[3].strip()))
            time_wait = int(lines[4].strip())
            logger.debug("conf_valid")
            logger.debug(in0)
            logger.debug(dir0)
            logger.debug(start0)
            logger.debug(user0)
            if ValueError or IndexError or NameError or BufferError or TypeError or SyntaxError:
                logger.debug("conf_invalid")
                pass


# run Area
if __name__ == "__main__":
    while running:
        config()
        time.sleep(time_wait)
        with open(start0, "r") as f:
            start = f.read().strip()
            if start == "Start!":
                User()
            if start == "Exit!":
                logger.warning("Exit!")


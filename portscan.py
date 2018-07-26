import tkinter, socket, os
import tkinter.messagebox
from datetime import datetime

#This Python Port Scanner/Banner Grabber is an easy way to gather some basic info about the security posture
#of an IP. It works by utilizing the Python socket module to use your device's built in network card to send a request
#to each port of the target IP. If the port is open it will reply with some information that will be used to indicate
#within the program if the port is open; if there is no response the port is not listed. Users are able to enter in
#the target IP and start/end range of the ports. It will automatically resolve a website to an IP and also features
#built in error checking that will prompt the user how to resolve the issue if one occurs. The results are output to
#a txt file named scanresults in the same directory as the program.


#Creates myGui class and initializes variables.
class myGui:
    def __init__(self):
        
        #Create main window.
        self.main_window = tkinter.Tk()

        #Create frames.

        self.host_frame = tkinter.Frame(self.main_window)

        self.host_resolve_frame = tkinter.Frame(self.main_window)

        self.port_start_frame = tkinter.Frame(self.main_window)

        self.port_start_confirm_frame = tkinter.Frame(self.main_window)

        self.port_end_frame = tkinter.Frame(self.main_window)

        self.port_end_confirm_frame = tkinter.Frame(self.main_window)

        self.port_result_frame = tkinter.Frame(self.main_window)

        self.button_frame = tkinter.Frame(self.main_window)

        #Create and pack widgets for host entry.

        self.host_label = tkinter.Label(self.host_frame, \
                                        text = 'Enter a remote host to scan:')
        
        self.host_entry = tkinter.Entry(self.host_frame, width = 25)

        self.host_label.pack(side='left')

        self.host_entry.pack(side='left')

        #Create and pack widgets for host resolution.
        
        self.host_resolve_label = tkinter.Label(self.host_resolve_frame, \
                                                text = 'Resolved host:')
        self.host_value = tkinter.StringVar()

        self.resolve_label = tkinter.Label(self.host_resolve_frame, \
                                           textvariable = self.host_value)

        self.resolve_button = tkinter.Button(self.host_resolve_frame, \
                                             text = 'Confirm IP', \
                                             command = self.hostIP)

        self.host_resolve_label.pack()

        self.resolve_label.pack()

        self.resolve_button.pack(side = 'left')

        #Create and pack widgets for Port Start

        self.port_start_label = tkinter.Label(self.port_start_frame, \
                                              text = 'Enter port beginning range:')
        
        self.port_start_entry = tkinter.Entry(self.port_start_frame, width = 12)
        
        self.port_start_label.pack(side='left')

        self.port_start_entry.pack(side='left')

        #Create and Pack Widgets for Port Start Confirm

        self.port_start_confirm_label = tkinter.Label(self.port_start_confirm_frame, \
                                                      text = "Confirm Port Start Range:")
        self.port_start_value = tkinter.StringVar()
        
        self.port_s_confirm_label = tkinter.Label(self.port_start_confirm_frame,\
                                          textvariable = self.port_start_value)

        self.port_start_confirm_button = tkinter.Button(self.port_start_confirm_frame, \
                                                        text = 'Confirm Port Start Range', \
                                                        command = self.minPortFunction)


        self.port_start_confirm_label.pack()
        
        self.port_s_confirm_label.pack()

        self.port_start_confirm_button.pack(side = 'left')
        

        #Create and Pack Widgets for Port End

        self.port_end_label = tkinter.Label(self.port_end_frame, \
                                            text = 'Enter port end range:')

        self.port_end_entry = tkinter.Entry(self.port_end_frame, width = 12)

        self.port_end_label.pack(side = 'left')

        self.port_end_entry.pack(side = 'left')

        #Create and pack widgets for Port End Confirm

        self.port_end_confirm_label = tkinter.Label(self.port_end_confirm_frame, \
                                                      text = "Confirm Port End Range:")
        self.port_end_value = tkinter.StringVar()
        
        self.port_e_confirm_label = tkinter.Label(self.port_end_confirm_frame,\
                                          textvariable = self.port_end_value)

        self.port_end_confirm_button = tkinter.Button(self.port_end_confirm_frame, \
                                                        text = 'Confirm Port End Range', \
                                                        command = self.maxPortFunction)
        
        self.port_end_confirm_label.pack()
        
        self.port_e_confirm_label.pack()

        self.port_end_confirm_button.pack(side = 'left')

        #Create and pack widgets for Port Result

        self.port_result_label = tkinter.Label(self.port_result_frame,\
                                               text = "Scan Results:")

        self.port_result_value = tkinter.StringVar()

        self.scan_result_label = tkinter.Label(self.port_result_frame,\
                                               textvariable = self.port_result_value)

        self.port_result_label.pack()

        self.scan_result_label.pack()

        #Create and pack widgets for the Buttons

        self.start_button = tkinter.Button(self.button_frame,\
                                           text = 'Start Scan',\
                                           command = self.portResult)

        self.quit_button = tkinter.Button(self.button_frame,\
                                          text = 'Quit',\
                                          command = self.main_window.destroy)

        self.help_button = tkinter.Button(self.button_frame, \
                                          text = 'Help', \
                                          command = self.help)

        self.start_button.pack(side = 'left')

        self.help_button.pack(side = 'left')
                                                        
        self.quit_button.pack(side = 'left')

        #Pack Frames
        
        self.host_frame.pack()

        self.host_resolve_frame.pack()

        self.port_start_frame.pack()

        self.port_start_confirm_frame.pack()

        self.port_end_frame.pack()

        self.port_end_confirm_frame.pack()

        self.port_result_frame.pack()

        self.button_frame.pack()
        
#Defines help functiont that displays the green info when the help button is pressed.
    def help(self):
        tkinter.messagebox.showinfo("Hello!", "Welcome to Python Port Scanner and Banner Grabber! /"
                                    "This program will scan the open ports on the IP you target to tell you/"
                                    "what kinf of information it is accepting. This is an easy way to determine/"
                                    "security of a website or PC. "
                                    "To use, enter the website/IP address you would like to scan and press /"
                                    "each corresponding button to lock in values. Common ports can be found /"
                                    "20-100 so it is recommended you start there if you are unsure. /"
                                    "Depending on the port range /"
                                    "selected the program can take a few wminutes to run. It will indicate /"
                                    "if the scan was successful or if an error occurred, and results will /"
                                    "be output in a file named scanresults.txt in the same directory as the /"
                                    "program. Thanks for using!")

#hostIP functions resolves the user inputted host into an IP if it is a website, or else confirms the IP.
    def hostIP(self):
        host = self.host_entry.get()
        try:
            hostIP  = socket.gethostbyname(host)
        except socket.gaierror:
            hostIP = ("Hostname could be resolved.")
        self.host_value.set(hostIP)

#Allows user to confirm the minimum port and verifies valid entry.
    def minPortFunction(self):
            try:
                minPort = int(self.port_start_entry.get())
            except ValueError:
                self.port_start_value.set("You need to enter a number.")
            if 1 > int(minPort) or 49150 < int(minPort):
                self.port_start_value.set("Invalid entry, please enter a number between 0 and 49151.")
            else:
                self.port_start_value.set(minPort)
                
#Allows user to confirm the maximum port and verifies valid entry.
    def maxPortFunction(self):
        minPort = int(self.port_start_entry.get())
        try:
            maxPort = int(self.port_end_entry.get())
        except ValueError:
            self.port_end_value.set("You need to enter a number.")
        if int(minPort) > int(maxPort) or int(maxPort) > 49151:
            self.port_end_value.set("Invalid entry. Please try again (49151 is limit.)")
        else:
            self.port_end_value.set(maxPort)

#portResults is the main function of the program. It begins with a dictionary of common ports that is used to help
#translate the results. It opens the scanresults file and writes to it (so each time it is new.) It incorporates
#the hostIP, minport and maxport functions to use as parameters for the program. It checks to see if a port is open
#and outputs the result if it is, skipping closed ports. It also has error handling in case a connection issue occurs.
#lastly it writes the result to an output file.
    def portResult(self):
            ports = {110:'POP3', 119:'NNTP', 123:'NTP', 137:'NetBIOS', 138:'NetBIOS',\
         139:'NetBIOS', 143:'IMAP', 22:'SSH', 161:'SNMP', 162:'SNMP',\
         23:'Telnet', 25:'SMTP', 49:'TACACS', 53:'DNS', 67:'DHCP(Server)',\
         68:'DHCP(Client)', 69:'TFTP', 80:'HTTP', 88:'Kerberos', 443:'HTTPS',\
         445:'SMB', 1701:'L2TP', 1720:'H.323', 1723:'PPTP', 1812:'RADIUS', \
         1813:'RADIUS', 2427:'MGCP', 2727:'MGCP', 3389:'RDP', 20:'FTP', \
         21:'FTP(Transfer)', 389:'LDAP'}
            results = open("scanresults.txt", "w")
            t1 = datetime.now()
            host = self.host_entry.get()
            hostIP = self.host_value.get()
            portStart = int(self.port_start_entry.get())
            portEnd = int(self.port_end_entry.get())
            tkinter.messagebox.showinfo("Welcome to Python Port Scanner and Banner Grabber!", "Please wait while scan runs.")
            self.port_result_value.set("Please wait, scanning host: " + host + " IP: " + hostIP + "\n")
            results.write("Please wait, scanning host: " + host + " IP: " + hostIP)
            for port in range(portStart, portEnd):
                try:
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    result = sock.connect_ex((host, port))
                    socket.setdefaulttimeout(0.4)
                    if result == 0:
                        try:
                            s = socket.socket()
                            s.connect((host, port))
                            banner = str(s.recv(1024))
                        except:
                            pass
                        if port in ports:
                            service = ports[port]
                        else:
                            service = "Not in common ports list- sorry!"
                        answer = ("\n Open Port: "+ str(port) + " Service: "+ str(service))
                        results.write(answer)
                        try:
                            results.write("\n" + banner)
                        except NameError:
                            pass
                        results.write('\n')
                        banner = "No banner found."
                    else:
                        answer = ("\n Port: "+ str(port) +" is closed.")
                        results.write(answer)
                        
    #Ends program if hostname cannot be resolved.
                except socket.gaierror:
                    self.port_result_value.set('Hostname could not be resolved.')
                    
    #Ends program if connection is not made.
                except socket.error:
                    self.port_result_value.set("Couldn't connect to server")
                    
        # Check what time scan ended
            t2 = datetime.now()

        #Calculates script run time
            total =  t2 - t1

        # Printing the information to screen
            self.port_result_value.set("Scan successful! View results in scanresults.txt")
            results.write('\n Scanning Completed in: '+ str(total))
            tkinter.messagebox.showinfo("Welcome to Python Port Scanner and Banner Grabber!", "Scan complete!")
            
my_gui = myGui()

        

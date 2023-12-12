# Creator: Eric Dennis
# Project Started: December 9th, 2023
# Last Updated (Update Summary): 
# Purpose: Building a portfolio website to showcase my skills to employers.


# -- Imports -- #

#4865cf
import streamlit as st
import streamlit_nested_layout
import streamlit.components.v1 as stcomp


from streamlit_carousel import carousel
from streamlit_option_menu import option_menu


# -- Building the Webpage -- #


# Streamlit configurations.
st.set_page_config(layout = "centered")

# Styling
st.write('''<style>
        
        .st-emotion-cache-1y4p8pa {
            max-width: 1080px;
        }

        </style>''', unsafe_allow_html=True)


# Creating the main menu.
selected = option_menu("", ["Home", "Jobs", "Projects", 'LinkedIn'], 
    icons = ['house', 'person-workspace', 'pencil', 'linkedin'], 
    menu_icon = "cast", default_index = 0, orientation = "horizontal",
    styles = {
        "nav-link-selected": {"font-weight": "600 !important"}
    }
)

# Home tab.
if selected == "Home":

    # Creating the home page.

    st.title("Hi, I'm Eric Dennis! 👋🏻")
    st.write('')
    st.markdown('''
                Hi, I'm Eric Dennis, a senior at Georgia Southern University majoring in Networks/Cybersecurity under Information Technology, set to graduate in Fall 2024.
                ''')

    st.image("https://www.thesimplebeliever.com/wp-content/uploads/2023/12/image.jpg",width=500)
    st.write('')
    st.subheader("My Academics")
    st.markdown('''
                My passion for understanding network intricacies and security has driven my academic success, landing me on the President's list seven times with a 4.0 GPA. I'm dedicated to mastering network administration complexities.\n
                ''')

    st.write('')
    st.subheader("My Skills and Abilities")
    st.markdown('''
                I have a sharp understanding of evolving network landscapes and emerging threats. Using my analytical skills, I identify vulnerabilities and implement robust security measures to protect critical infrastructures and data.\n
                My goal is to fortify network architectures, defending against cyber threats. I'm excited about contributing to network security advancements, creating a safer digital environment for everyone.
                ''')
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.button("Python")
        st.button("CSS")
        st.button("Windows")
    with col2:
        st.button("Networking")
        st.button("MySQL")
        st.button("Linux")
    with col3:
        st.button("Routers")
        st.button("SQL")
        st.button("Cloud Computing")
    with col4:
        st.button("Switches")
        st.button("SQLite")
        st.button("Cybersecurity")
    with col5:
        st.button("HTML")
        st.button("WordPress")
        st.button("Joomla")
    
    st.write("")
    st.subheader("Certifications")
    st.markdown("Electronic Document Associate (EDA)")
    st.caption('''Xplor International · Issued Aug 2023''')

# Job tab.
if selected == "Jobs":
    
    st.title("Experience! 👨🏼‍💻")
    st.header("Solutions Development Intern")
    st.caption("Quantre Solutions · Jan 2023 - Sep 2023 · 9 mos")
    st.caption("Atlanta Metropolitan Area · Hybrid")
    st.markdown('''
                As a team member, I am responsible for supporting the development of innovative solutions for our clients by collaborating closely with my colleagues to design, develop, and implement web applications that meet their needs. Specifically, I:
                \n
                &nbsp;&nbsp;&nbsp;&nbsp;• Create PowerBI & Python visuals to transform complex data into easy-to-understand insights.\n
                &nbsp;&nbsp;&nbsp;&nbsp;• Aid in the data analysis process and identify trends in large datasets to support decision-making.\n
                &nbsp;&nbsp;&nbsp;&nbsp;• Collaborate with the team to develop cutting-edge solutions that improve client satisfaction.\n
                &nbsp;&nbsp;&nbsp;&nbsp;• Design, develop, and test web applications using industry-standard frameworks and tools to ensure high-quality output.\n
                &nbsp;&nbsp;&nbsp;&nbsp;• Participate in project reviews and work with the team to improve application functionality and usability.\n
                &nbsp;&nbsp;&nbsp;&nbsp;• Research and implement new technologies to enhance the application development process, enabling us to deliver projects more efficiently.\n
                \n
                By contributing my technical expertise and collaborating with the team, I help ensure that our projects are delivered on time and to the satisfaction of our clients. I am committed to staying up-to-date with the latest technologies and continuously improving our processes to deliver exceptional results.
                ''')
    st.link_button("Link to One of the Projects", "https://wiki.xplor.org/index.php?title=Main_Page")
    st.caption("Skills: Microsoft Access · HTML · Cascading Style Sheets (CSS) · Joomla! · SQL · Python (Programming Language) · Content Management Systems (CMS) · Data Analysis")
    
    st.header("Video Editor")
    st.caption("Freelance · Self-employed (Remote)")
    st.caption("Oct 2017 - Aug 2022 · 4 yrs 11 mos")
    st.markdown('''
                As a former video editor, I had the opportunity to work with individuals from diverse backgrounds and bring their creative visions to life. During my time in this role, I acquired essential technical skills that expanded my knowledge and fueled my passion for the art of technology.
                ''')
    st.caption("Skills: Wondershare Filmora")
    
# Projects tab.
if selected == "Projects":
    
    st.title("Projects ✏️")
    st.write("")
    st.subheader("Personal Projects")
    
        
    # Setting Up Pi-Hole and Pi-VPN on AWS.
    with st.expander("Setting Up Pi-Hole and Pi-VPN on AWS"):
        st.header("Setting Up Pi-Hole and Pi-VPN on AWS")
        st.caption("December 2023")
        
        st.subheader("Pi-Hole")
        st.markdown('''
            To enhance online anonymity and block excessive ads, I opted to host a DNS/VPN server on Amazon's AWS using Lightsail's Ubuntu 22.04 LTS OS.
            Here's a step-by-step guide of the process:
            ''')

        # SSH into the AWS Lightsail server
        st.markdown("1. **SSH Access**: Connect to the server via SSH.")

        # Update and install Pi-Hole
        st.markdown("2. **Update and Install Pi-Hole**: Ensure the system is up-to-date and install Pi-Hole.")
        st.code("sudo apt update && sudo apt upgrade -y \ncurl -sSL https://install.pi-hole.net | bash")

        # Pi-Hole setup interface and configurations
        st.markdown("3. **Pi-Hole Setup**:")
        st.markdown("- In the Pi-Hole setup interface, choose the appropriate network interface (e.g., 'eth0' for Ethernet connectivity). Since I am working with an AWS server, there is no wlan0 (Wi-Fi) option.")
        st.code("(*) eth0   available")

        st.markdown("- The following lists are preconfigured blocklists. I only selected StevenBlack's list as I will be added third-party lists later.")
        st.code('''
                [*] StevenBlack    StevenBlack's Unified Hosts List\n
                [ ] MalwareDom     MalwareDomains\n
                [ ] Cameleon       Cameleon\n
                [ ] ZeusTracker    Zeus Tracker\n
                [ ] Discon Track   Disconnect.me Tracking\n
                [ ] DisconAd       Disconnect.me Ads\n
                [ ] HostsFile      Hosts-file.net Ads
                ''')
        
        st.markdown("- Select DNS providers and blocklists based on preferences. I decided to use Google. Once the DNS requests have been filtered by Pi-Hole, the requests will then be sent to Google's DNS servers to be resolved.")
        st.code('''
                [*] Google\n
                [ ] OpenDNS\n
                [ ] Level3\n
                [ ] Comodo\n
                [ ] DNSWatch\n
                [ ] Quad9\n
                [ ] FamilyShield
                ''')

        st.markdown("4. **Firewall Configuration**: Open firewall to accept DNS requests on port 53 (TCP and UDP). Since I am using AWS Lightsail, I went to the network configuration tab, attached a static IP address, and opened up port 53 to accept DNS requests. :red[The following IP address is fake for the sake of security. It has been changed.]")
        st.image("https://www.thesimplebeliever.com/wp-content/uploads/2023/12/Lightsail.png", width=500)

        st.markdown("5. **Additional Filters/Blocklists**:")
        st.markdown("- Access Pi-Hole's web interface to add more lists from firebog.net.")
        st.image("https://www.thesimplebeliever.com/wp-content/uploads/2023/12/Adlist.png", width=500)
        st.image("https://www.thesimplebeliever.com/wp-content/uploads/2023/12/finallist.png", width=500)

        st.markdown("6. **Update Lists**:")
        st.markdown("- Run the command to download and update the added lists.")
        st.code("pihole -g")

        st.markdown("7. **Configuration on Devices**:")
        st.markdown("- Configure device DNS settings to use the Pi-Hole's DNS server.")
        st.markdown("- For example, on Windows 11: Settings > Network & Internet > Wi-Fi > Select Wi-Fi > DNS Server Assignment > Choose manual > Input DNS server's IPv4 address.")
        st.image("https://www.thesimplebeliever.com/wp-content/uploads/2023/12/Realtime-Blocking.png", width=500)

        st.markdown("Now, devices connected will have ads blocked through Pi-Hole.")

        st.write("")
        st.subheader("Pi-VPN")
        
        st.markdown("1. **Download and Install Pi-VPN**:")
        st.code("curl -L https://install.pivpn.io | bash")
        
        st.markdown("2. **Selecting the VPN Service**: ")
        st.markdown("I selected using WireGuard since it is the faster and newer option compared to OpenVPN.")
        st.code('''
                (*) WireGuard\n
                ( ) OpenVPN
                ''')
        
        st.markdown("3. **Selecting the Default Port and DNS Settings**")
        st.markdown("I stuck with the default port, which is 51820, for WireGuard. I also opened up port 51820 on AWS Lightsail. Additionally, since I am running Pi-Hole on the same server, I chose the custom option and input the servers IPv4 address for the DNS resolver. I will not show any photos here since it is essentially the same as setting up Pi-Hole above.")
        
        st.markdown("5. **Creating a User**")
        st.markdown("Next, using the following command, I created a profile for my phone called 'Eric'. ")
        
        st.markdown("5. **Downloading WireGuard for Mobile**")
        st.markdown("Going to Google Play, I downloaded the WireGuard app. After setting it up, I went back to my server and generated a QR to scan for my phone with the following command:")
        st.code("pivpn -qr\n")
        st.markdown("Once scanned, the a tunnel is created between the server and my phone for anonymity and ad-free browsing. This completes the installation of Pi-VPN for the server. An example is shown below:")
        
    with st.expander("Linux (Debian) Network/Server Dashboard Widget for WordPress"):
        st.header("Linux (Debian) Network/Server Dashboard Widget for WordPress")
        st.caption("Nov 2023 - Dec 2023")
        st.markdown('''
                    Starting on November 21st, 2023, I initiated a project to build a monitoring service. I aimed to connect to a Linux web server via SSH, extract network and server data, and present it through a user-friendly dashboard using Streamlit in Python.\n
                    Utilizing Python libraries like paramiko, pandas, streamlit, and plotly, I established a secure SSH connection to the server using a private key file and retrieved vital statistics.\n
                    I designed functions to execute commands remotely, capturing RAM usage, CPU statistics, uptime, bandwidth data for various periods, and global ping stats. These data were organized into a dictionary for efficient presentation.\n
                    Creating a Streamlit web app with 'Network' and 'Server' tabs, I displayed IP addresses, ports, bandwidth information, and global ping maps on the 'Network' tab. The 'Server' tab showcased real-time RAM, CPU usage, and server details.\n
                    To enable real-time monitoring, I programmed the dashboard to refresh every 10 seconds, updating live metrics such as RAM, CPU, and uptime.\n
                    Error handling was implemented to address potential authentication or SSH connection issues, providing clear error messages for troubleshooting.\n
                    This project aimed to provide an intuitive dashboard for seamless monitoring of a Linux web server's crucial statistics, allowing easy real-time visualization and tracking of network and server health.
                    ''')
        st.caption("Skills: Paramiko · Streamlit · CLI · CMD · Cloud Applications · Network Administration · Linux · Debian · Ubuntu · Cloud Computing · Servers · HTML · Cascading Style Sheets (CSS) · Python (Programming Language)")
        with st.expander("Full Python Code"):
            st.code('''
\n                
# Created By: Eric Dennis                
# Project Started: November 21st, 2023
# Last Updated (Update Summary): n/a
# Purpose: Connect via SSH to Linux Web Server to extract server information and build a monitoring service.

# Importing modules / libraries.
import time
import paramiko
import streamlit as st

from PIL import Image


#####################
# Server Connection #
#####################

# Web server connection details for "_________.com".
port = st.secrets['ports']
username = st.secrets['username']
hostname = st.secrets['ip']
private_key_path = "pk.pem"


# Create an SSH client and load the private key.
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
private_key = paramiko.RSAKey.from_private_key_file(private_key_path)

# Connecting to the server.
ssh.connect(hostname, port, username, pkey = private_key)


######################
# Defining Functions #
######################

# Function to update the RAM metric value.
def update_ram_usage():
    stdin, stdout, stderr = ssh.exec_command('free | awk \'/Mem:/ {printf "%.0f\\n", $3/$2 * 100.0}\'')

    # Answer
    result = stdout.read().decode().strip()
    error = stderr.read().decode().strip()

    return result


# Function to update the CPU metric value
def update_cpu_usage():
    stdin, stdout, stderr = ssh.exec_command('sar -u 1 1 | tail -n 1 | awk \'{printf "%.0f", $3}\'')

    # Answer
    current_cpu = stdout.read().decode().strip()
    current_cpu = str(current_cpu)

    return current_cpu


# Function to update the uptime metric
def uptime():
    stdin, stdout, stderr = ssh.exec_command("uptime | awk -F'[ ,]+' '{print $4 \" days\"}'")

    # Answer
    result = stdout.read().decode().strip()
    error = stderr.read().decode().strip()

    return result


##########################
# Various Other Commands #
##########################

# Initialize a dictionary to store results
commands = [
    #Network
    "ip route get 1.2.3.4 | awk '{print $7}'", #Hostname
    "curl ipinfo.io/ip", #Public IP
    "grep 'nameserver' /etc/resolv.conf | awk '{print $2}'", #DNS Server
    "netstat -e -n -i | grep ens5 -A 1 | grep 'inet' | tail -1 | awk '{print $4}'", #Subnet Mask
    "sudo ss -tulpn | grep LISTEN | awk '{print $5}' | awk -F: '{print $NF}'", #Ports
    "ip -o -brief link show | awk '{print $1}'", #NICs
    "netstat -e -n -i | grep ens5 -A 5 | grep 'RX packets' | tail -1 | awk '{print $6$7}' | sed 's/[()]//g'", #Recieved Packets
    "netstat -e -n -i | grep ens5 -A 7 | grep 'TX packets' | tail -1 | awk '{print $6$7}' | sed 's/[()]//g'", #Transmitted Packets

    #Server
    'echo "$(uname -s) ($(getconf LONG_BIT)-bit)"', #OS
    'lsb_release -sd | awk \'{printf "%s (v. %s)\\n", $1, $3}\'', #Type/Version
    "grep 'VERSION_CODENAME' /etc/os-release | cut -d= -f2", #Version Codename
    "stat -c '%y' /var/log/dpkg.log | awk -F. '{print $1}' | awk '{print $1}'", #Last Updated
    "nproc --all", #CPU Cores
    'lscpu | grep "Hypervisor vendor:" | awk -F: \'{print $2}\' | tr -s " "', #Hypervisor
    "lscpu | grep 'Model name' | awk -F': ' '{print $2}'", #CPU Model
    "free -h | awk '/^Mem:/ {print $2}'", #RAM
    "df -h /dev/nvme0n1p1 | awk 'NR==2 {print $5}'" #Storage
]


cmd_data = [
    #Network
    "Hostname", 
    "Public IP",
    "DNS Server",
    "Subnet Mask",
    "Ports",
    "NICs",
    "Recieved Packets",
    "Transmitted Packets",

    #Server
    "OS",
    "Type/Version",
    "Version Codename",
    "Last Updated",
    "CPU Cores",
    "Hypervisor",
    "CPU Model",
    "RAM",
    "Storage"
]

results = {}

# Run the commands and pair results with data
for command, data in zip(commands, cmd_data):
    stdin, stdout, stderr = ssh.exec_command(command)
    result = stdout.read().decode().strip()
    error = stderr.read().decode().strip()

    if data == "Ports":
        # Split the result by newline, remove duplicates, convert to integers, and then sort
        result = sorted(map(int, set(result.split('\n'))))
        result = ', '.join(map(str, result))

    if data == "NICs":
        # Split the result by newline, remove duplicates, convert to integers, and then sort
        result = sorted(map(str, set(result.split('\n'))))
        result = ', '.join(map(str, result))

    results[data] = result


#################
# Streamlit App #
#################

# Streamlit app with configurations.
st.set_page_config(layout = "centered")
st.title('Network/Server Monitor 🌳')

# Establishing tabs for server and network.
tab1, tab2 = st.tabs(["Network", "Server"])
    

###############
# Network Tab #
###############

with tab1:

    st.write("")
    st.subheader("Basic Network Info")
    
    image = Image.open("C:\\Users\\ericd\\summary.png")
    st.image(image, caption='Remote Image', use_column_width="always")

    # Creating columns for the network information.
    col9, col10, col11 = st.columns(3)

    with col9:
        st.metric(label = "Hostname", value = results["Hostname"])
        st.metric(label = "Open Ports", value = results["Ports"])
    with col10:
        st.metric(label = "Public IP", value = results["Public IP"])
        st.metric(label = "NICs", value = results["NICs"])
    with col11:
        st.metric(label = "DNS Server", value = results["DNS Server"])
        st.metric(label = "Subnet Mask", value = results["Subnet Mask"])

    #Bandwidth Information
    st.write("")
    st.subheader("Bandwidth Info")

    col12, col13, col14 = st.columns(3)

    with col12:
        st.metric(label = "Total RX", value = results["Recieved Packets"])
    with col13:
        st.metric(label = "Total TX", value = results["Transmitted Packets"])
    with col14:
        st.write("")
        
print("hello")
##############
# Server Tab #
##############

with tab2:

    # Header information.
    st.write("")
    st.subheader("Live RAM & CPU Usage, Uptime 🕖")

    # First row of columns used for refreshed data.
    col1, col2, col3 = st.columns(3)

    # Initial metric value.
    with col1:
        metric_ram_value = st.metric(label = "RAM", value = update_ram_usage() + "%") # Initial RAM
    with col2:
        metric_cpu_value = st.metric(label = "CPU", value = update_cpu_usage() + "%") # Initial CPU
    with col3:
        metric_uptime = st.metric(label = "Uptime", value = str(uptime())) # Initial Uptime

    # Layout design.
    with st.container():
        st.write("")
        st.write("")


    # General server information.
    st.subheader("Random Server Info 📈")

    # Creating columns for the general server information.
    col6, col7, col8 = st.columns(3)

    with col6:
        st.metric(label = "OS", value = results["OS"])
        st.metric(label = "Last Updated", value = results["Last Updated"])
    with col7:
        st.metric(label = "Type/Version", value = results["Type/Version"])
        st.metric(label = "CPU Cores", value = results["CPU Cores"])
    with col8:
        st.metric(label = "Codename", value = results["Version Codename"].capitalize())
        st.metric(label = "Hypervisor", value = results["Hypervisor"])

    # Layout design.
    with st.container():
        st.write("")
        st.write("")

    #SSD and PHP
    st.subheader("Storage & PHP")

    st.progress(int(results['Storage'].rstrip('%')), "Storage Used (SSD): " + str(results["Storage"]))


# Continuously update various metrics on the dashboard every 3 seconds.
while True:
    time.sleep(10)

    metric_ram_value.metric(label = "RAM", value = str(update_ram_usage()) + "%") # RAM
    metric_cpu_value.metric(label = "CPU", value = update_cpu_usage() + "%") # CPU
    metric_uptime.metric(label = "Uptime", value = str(uptime())) # Uptime
''')
            images = [
                dict(title="Network Tab", text="", interval=None, img="https://www.thesimplebeliever.com/wp-content/uploads/2023/12/Network-Tab.png"),
                dict(title="Server Tab", text="", img="https://www.thesimplebeliever.com/wp-content/uploads/2023/12/Server-Tab.png"),
            ]
        carousel(items=images)
        st.video("https://www.thesimplebeliever.com/wp-content/uploads/2023/12/video-example.mp4")
    st.write("")
      
      
    st.subheader("Work Projects")  
    
    
    #
    with st.expander("CMS Modernization: Enhanced UX with Workflow Automations and Cloud API Integrations"):
        st.header("CMS Modernization: Enhanced UX with Workflow Automations and Cloud API Integrations")
        st.caption("Jan 2023 - Jun 2023")
        st.caption("Associated with Quantre Solutions")
        st.markdown('''
                    Content Management System (CMS) modernization project, revolutionizing the user experience through a guided workflow utilizing geo-location personalizations to automate and validate user data submissions. By integrating Google and Azure APIs, the project team extended the base system’s data definition, capture, and validation capacity, culminating in a robust, automated workflow.
                    \n
                    Our team's relentless pursuit of excellence transformed the platform into an advanced service delivery and reporting solution. This initiative replaced antiquated manual processing with a secure automated service and a modern digital reporting service. This paradigm shift improved efficiency, enhanced data security, and delivered an enriched user experience.
                    ''')
        st.caption("Skills: Cloud Computing · Google Cloud Platform (GCP) · Microsoft Power BI · Workflow Automation · Data Validation · User Experience Design (UED) · API · SQL · Python (Programming Language) · Content Management Systems (CMS) · Data Analysis")
        
    #
    with st.expander('Wiki Site Deployment & Migration of "A Guide to the Electronic Document Body of Knowledge" for Xplor International'):
        st.header('Wiki Site Deployment & Migration of "A Guide to the Electronic Document Body of Knowledge" for Xplor International')
        st.caption("Apr 2023 - Jul 2023")
        st.caption("Associated with Quantre Solutions")
        st.markdown('''
                    Spearheaded the successful deployment of a wiki site using MediaWiki and Wikimedia Commons for Xplor International. The project included: \n
                    &nbsp;&nbsp;&nbsp;&nbsp;• Installing and configuring MediaWiki technology\n
                    &nbsp;&nbsp;&nbsp;&nbsp;• UI branding and customization for a mobile experience\n
                    &nbsp;&nbsp;&nbsp;&nbsp;• Designing user onboarding experience and governance mod\n
                    &nbsp;&nbsp;&nbsp;&nbsp;• Deployed modules for UI skins, rich text editing, HTML parsing, InfoBox templates, and citations.\n
                    &nbsp;&nbsp;&nbsp;&nbsp;• Configured NonCommercial and ShareAlike license models for content \n
                    &nbsp;&nbsp;&nbsp;&nbsp;• Configured CSS files to match publication branding\n
                    &nbsp;&nbsp;&nbsp;&nbsp;• Image transformation and migrations\n
                    &nbsp;&nbsp;&nbsp;&nbsp;• Configured and deployed organizational event marketing\n
                    &nbsp;&nbsp;&nbsp;&nbsp;• Developed Agile content deployment plan\n
                    &nbsp;&nbsp;&nbsp;&nbsp;• Digital Transformation of "A Guide to the Electronic Document Body of Knowledge" published by Xplor International in 2014, into interactive and user-friendly wiki content.
                    ''')
        st.link_button("Link to the Website", "https://wiki.xplor.org/index.php?title=Main_Page")
        st.caption("Skills: Digital Transformation · User Experience Design (UED) · Software Development Life Cycle (SDLC) · HTML · Content Management Systems (CMS)")
        
        
# LinkedIn tab.
if selected == "LinkedIn":
    st.link_button("Link to my LinkedIn Profile", "https://www.linkedin.com/in/ericdennis7/", use_container_width=True)
    

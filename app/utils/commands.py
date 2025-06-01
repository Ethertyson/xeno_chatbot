windows_cmds = {
    # Create directory
    "how do i make a directory in windows": "mkdir DIRECTORY_NAME",
    "how do i create a directory in windows": "mkdir DIRECTORY_NAME",
    "how to make a folder in windows": "mkdir DIRECTORY_NAME",
    "how to create a folder in windows": "mkdir DIRECTORY_NAME",
    "command to create directory in windows": "mkdir DIRECTORY_NAME",
    "command to make folder in windows": "mkdir DIRECTORY_NAME",
    "how can i make a directory in windows": "mkdir DIRECTORY_NAME",
    "how can i create a folder in windows": "mkdir DIRECTORY_NAME",
    "windows mkdir command": "mkdir DIRECTORY_NAME",

    # Delete file or folder
    "how to delete a file in windows": "del FILE_NAME",
    "how do i delete a file in windows": "del FILE_NAME",
    "how to remove a file in windows": "del FILE_NAME",
    "command to delete file in windows": "del FILE_NAME",
    "how to delete a folder in windows": "rmdir /s DIRECTORY_NAME",
    "how do i delete a folder in windows": "rmdir /s DIRECTORY_NAME",
    "command to remove directory in windows": "rmdir /s DIRECTORY_NAME",
    "remove folder in windows command": "rmdir /s DIRECTORY_NAME",
    "delete directory in windows": "rmdir /s DIRECTORY_NAME",
    "remove directory in windows": "rmdir /s DIRECTORY_NAME",

    # Copy files
    "how to copy a file in windows": "copy SOURCE DESTINATION",
    "how do i copy files in windows": "copy SOURCE DESTINATION",
    "command to copy file in windows": "copy SOURCE DESTINATION",
    "copy file command windows": "copy SOURCE DESTINATION",
    "copy folder in windows": "xcopy SOURCE DESTINATION /E /I",

    # Move files
    "how to move a file in windows": "move SOURCE DESTINATION",
    "how do i move files in windows": "move SOURCE DESTINATION",
    "command to move file in windows": "move SOURCE DESTINATION",
    "move file command windows": "move SOURCE DESTINATION",

    # List directory contents
    "how to list files in windows": "dir",
    "how do i list directory contents in windows": "dir",
    "command to list files in windows": "dir",
    "show files in folder windows": "dir",
    "list directory windows": "dir",

    # Clear screen
    "how to clear the screen in windows": "cls",
    "clear terminal windows": "cls",
    "command to clear screen in windows": "cls",

    # Show IP config
    "how to show ip address in windows": "ipconfig",
    "how do i check ip in windows": "ipconfig",
    "command to display ip config windows": "ipconfig",

    # Ping command
    "how to ping in windows": "ping ADDRESS",
    "ping command windows": "ping ADDRESS",
    "how do i test connectivity in windows": "ping ADDRESS",

    # Task list/processes
    "how to list running processes in windows": "tasklist",
    "show running processes windows": "tasklist",
    "command to view processes in windows": "tasklist",

    # Kill task/process
    "how to kill a process in windows": "taskkill /PID PROCESS_ID /F",
    "command to stop task in windows": "taskkill /PID PROCESS_ID /F",
    "terminate process windows command": "taskkill /PID PROCESS_ID /F",

    # System info
    "how to get system info in windows": "systeminfo",
    "show system information windows": "systeminfo",
    "command to display system info windows": "systeminfo",

    # Network config (advanced)
    "how to release ip in windows": "ipconfig /release",
    "how to renew ip in windows": "ipconfig /renew",
    "flush dns cache windows": "ipconfig /flushdns",
    "clear dns cache windows": "ipconfig /flushdns",

    # User management
    "how to add a user in windows": "net user USERNAME PASSWORD /add",
    "command to create user windows": "net user USERNAME PASSWORD /add",
    "delete user windows command": "net user USERNAME /delete",

    # Check disk usage
    "how to check disk usage in windows": "chkdsk",
    "command to check disk windows": "chkdsk",

    # Change directory
    "how to change directory in windows": "cd DIRECTORY_PATH",
    "navigate folder windows command": "cd DIRECTORY_PATH",

    # Show environment variables
    "how to show environment variables in windows": "set",
    "list env variables windows": "set",

    # IP config detailed
    "show detailed ip info windows": "ipconfig /all",

    # Shutdown and restart
    "how to shutdown windows from command line": "shutdown /s /t 0",
    "how to restart windows from command line": "shutdown /r /t 0",

    # Disk partition list
    "list disk partitions windows": "diskpart",

    # Format drive
    "format drive windows": "format DRIVE_LETTER:",

    # Network connections
    "show active network connections windows": "netstat -an",

    # Wireless networks
    "show wireless networks windows": "netsh wlan show profiles",
    "show saved wifi passwords windows": "netsh wlan show profile name=PROFILE_NAME key=clear",

    # IP config renew and release
    "release ip address windows": "ipconfig /release",
    "renew ip address windows": "ipconfig /renew",

    # Powercfg (battery info)
    "show battery report windows": "powercfg /batteryreport",

    # System file checker
    "run system file checker windows": "sfc /scannow",

    # Disk cleanup
    "run disk cleanup windows": "cleanmgr",

    # Display date and time
    "show date and time windows": "date /t && time /t",

    # View network config
    "show network config windows": "ipconfig /all",

    # Get help on commands
    "how to get help on a command windows": "command /?",
}



linux_cmds = {
    # Create directory
    "how do i make a directory in linux": "mkdir DIRECTORY_NAME",
    "how do i create a directory in linux": "mkdir DIRECTORY_NAME",
    "how to make a folder in linux": "mkdir DIRECTORY_NAME",
    "how to create a folder in linux": "mkdir DIRECTORY_NAME",
    "command to create directory in linux": "mkdir DIRECTORY_NAME",
    "command to make folder in linux": "mkdir DIRECTORY_NAME",
    "how can i make a directory in linux": "mkdir DIRECTORY_NAME",
    "how can i create a folder in linux": "mkdir DIRECTORY_NAME",
    "linux mkdir command": "mkdir DIRECTORY_NAME",

    # Delete file or folder
    "how to delete a file in linux": "rm FILE_NAME",
    "how do i delete a file in linux": "rm FILE_NAME",
    "how to remove a file in linux": "rm FILE_NAME",
    "command to delete file in linux": "rm FILE_NAME",
    "how to delete a folder in linux": "rm -r DIRECTORY_NAME",
    "how do i delete a folder in linux": "rm -r DIRECTORY_NAME",
    "command to remove directory in linux": "rm -r DIRECTORY_NAME",
    "remove folder in linux command": "rm -r DIRECTORY_NAME",
    "delete directory in linux": "rm -r DIRECTORY_NAME",
    "remove directory in linux": "rm -r DIRECTORY_NAME",

    # Copy files
    "how to copy a file in linux": "cp SOURCE DESTINATION",
    "how do i copy files in linux": "cp SOURCE DESTINATION",
    "command to copy file in linux": "cp SOURCE DESTINATION",
    "copy file command linux": "cp SOURCE DESTINATION",
    "copy folder in linux": "cp -r SOURCE DESTINATION",

    # Move files
    "how to move a file in linux": "mv SOURCE DESTINATION",
    "how do i move files in linux": "mv SOURCE DESTINATION",
    "command to move file in linux": "mv SOURCE DESTINATION",
    "move file command linux": "mv SOURCE DESTINATION",

    # List directory contents
    "how to list files in linux": "ls",
    "how do i list directory contents in linux": "ls",
    "command to list files in linux": "ls",
    "show files in folder linux": "ls",
    "list directory linux": "ls",

    # Clear screen
    "how to clear the screen in linux": "clear",
    "clear terminal linux": "clear",
    "command to clear screen in linux": "clear",

    # Show IP config
    "how to show ip address in linux": "ip addr show",
    "how do i check ip in linux": "ip addr show",
    "command to display ip config linux": "ip addr show",
    "show ip address linux": "ip addr show",

    # Ping command
    "how to ping in linux": "ping ADDRESS",
    "ping command linux": "ping ADDRESS",
    "how do i test connectivity in linux": "ping ADDRESS",

    # Process list
    "how to list running processes in linux": "ps aux",
    "show running processes linux": "ps aux",
    "command to view processes in linux": "ps aux",

    # Kill task/process
    "how to kill a process in linux": "kill -9 PROCESS_ID",
    "command to stop task in linux": "kill -9 PROCESS_ID",
    "terminate process linux command": "kill -9 PROCESS_ID",

    # System info
    "how to get system info in linux": "uname -a",
    "show system information linux": "uname -a",
    "command to display system info linux": "uname -a",

    # Network config (advanced)
    "how to release ip in linux": "dhclient -r",
    "how to renew ip in linux": "dhclient",
    "flush dns cache linux": "sudo systemd-resolve --flush-caches",
    "clear dns cache linux": "sudo systemd-resolve --flush-caches",

    # User management
    "how to add a user in linux": "sudo adduser USERNAME",
    "command to create user linux": "sudo adduser USERNAME",
    "delete user linux command": "sudo deluser USERNAME",

    # Check disk usage
    "how to check disk usage in linux": "df -h",
    "command to check disk linux": "df -h",

    # Change directory
    "how to change directory in linux": "cd DIRECTORY_PATH",
    "navigate folder linux command": "cd DIRECTORY_PATH",

    # Show environment variables
    "how to show environment variables in linux": "printenv",
    "list env variables linux": "printenv",

    # Shutdown and restart
    "how to shutdown linux from command line": "sudo shutdown -h now",
    "how to restart linux from command line": "sudo shutdown -r now",
    "shutdown linux command": "sudo shutdown -h now",
    "restart linux command": "sudo shutdown -r now",

    # Disk partition list
    "list disk partitions linux": "lsblk",

    # Format drive
    "format drive linux": "mkfs -t FILESYSTEM_TYPE DEVICE",

    # Network connections
    "show active network connections linux": "netstat -tuln",

    # Wireless networks
    "show wireless networks linux": "nmcli dev wifi list",
    "show saved wifi passwords linux": "sudo grep -r '^psk=' /etc/NetworkManager/system-connections/",

    # Power management
    "show battery status linux": "upower -i $(upower -e | grep BAT)",
    
    # System file checker (Linux equivalent)
    "run file system check linux": "sudo fsck /dev/sdX",

    # Disk cleanup (Linux has multiple tools)
    "run disk cleanup linux": "sudo apt-get clean",  # For Debian/Ubuntu

    # Display date and time
    "show date and time linux": "date",

    # Get help on commands
    "how to get help on a command linux": "man COMMAND",
}

macos_cmds = {
    # Create directory
    "how do i make a directory in macos": "mkdir DIRECTORY_NAME",
    "how to create folder in macos": "mkdir DIRECTORY_NAME",
    "macos mkdir command": "mkdir DIRECTORY_NAME",
    "how do i create a folder in macos": "mkdir DIRECTORY_NAME",
    "create a new folder in macos": "mkdir DIRECTORY_NAME",
    "command to make directory macos": "mkdir DIRECTORY_NAME",

    # Delete files/folders
    "how to delete a file in macos": "rm FILE_NAME",
    "how to remove a file in macos": "rm FILE_NAME",
    "delete file using terminal macos": "rm FILE_NAME",
    "remove file command macos": "rm FILE_NAME",
    "how to delete a folder in macos": "rm -r DIRECTORY_NAME",
    "how to remove a directory in macos": "rm -r DIRECTORY_NAME",
    "delete folder command macos": "rm -r DIRECTORY_NAME",

    # Copy files/folders
    "how to copy a file in macos": "cp SOURCE DEST",
    "copy file command in macos": "cp SOURCE DEST",
    "macos command to copy files": "cp SOURCE DEST",
    "copy a folder in macos": "cp -r SOURCE DEST",
    "how to copy directory in macos": "cp -r SOURCE DEST",

    # Move/Rename files
    "how to move a file in macos": "mv SOURCE DEST",
    "move command in macos": "mv SOURCE DEST",
    "how to rename a file in macos": "mv OLD_NAME NEW_NAME",
    "rename command macos": "mv OLD_NAME NEW_NAME",

    # List contents
    "how to list files in macos": "ls",
    "list all files including hidden in macos": "ls -a",
    "list with details in macos": "ls -l",
    "see files in folder macos": "ls",
    "show contents of directory in macos": "ls",

    # Clear screen
    "how to clear terminal in macos": "clear",
    "clear screen command macos": "clear",

    # Change directory
    "how to change directory in macos": "cd DIRECTORY_NAME",
    "go back one directory macos": "cd ..",
    "go to home directory macos": "cd ~",
    "navigate folders in macos terminal": "cd DIRECTORY_NAME",

    # Show current directory
    "what is the current directory in macos": "pwd",
    "macos current working directory command": "pwd",

    # Permissions
    "how to change file permissions in macos": "chmod MODE FILE",
    "make file executable in macos": "chmod +x FILE",
    "chmod command macos": "chmod +x FILE",
    "how to change file owner in macos": "chown USER FILE",

    # File search
    "how to search for a file in macos": "find / -name FILE_NAME",
    "find a folder in macos": "find / -type d -name FOLDER_NAME",
    "command to locate files in macos": "find / -name FILE_NAME",

    # View file content
    "how to view a file in terminal macos": "cat FILE_NAME",
    "see top lines of file macos": "head FILE_NAME",
    "see bottom lines of file macos": "tail FILE_NAME",

    # Disk usage
    "how to check disk usage in macos": "df -h",
    "check folder size macos": "du -sh FOLDER_NAME",

    # Running processes
    "how to see running processes in macos": "ps aux",
    "macos task manager in terminal": "top",

    # Kill a process
    "how to kill a process in macos": "kill PID",
    "how to force kill in macos": "kill -9 PID",

    # Shutdown / Reboot
    "how to shutdown macos using terminal": "sudo shutdown -h now",
    "how to restart macos in terminal": "sudo shutdown -r now",

    # Network
    "how to check ip address in macos": "ifconfig",
    "how to test network in macos": "ping ADDRESS",
    "check open ports macos": "netstat -an",

    # Archive / Unzip
    "how to unzip file in macos": "unzip FILE.zip",
    "how to zip folder in macos": "zip -r ARCHIVE.zip FOLDER",
    "compress folder macos": "zip -r ARCHIVE.zip FOLDER",

    # Package management (Homebrew)
    "how to install homebrew in macos": "/bin/bash -c \"$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)\"",
    "install a package with homebrew in macos": "brew install PACKAGE_NAME",
    "update brew packages in macos": "brew update",
    "list installed brew packages in macos": "brew list",
    "remove a brew package in macos": "brew uninstall PACKAGE_NAME",

    # Python & pip
    "install a python package in macos": "pip install PACKAGE_NAME",
    "check python version in macos": "python3 --version",
    "run a python script in macos": "python3 script.py",

    # Git
    "clone repo in macos": "git clone REPO_URL",
    "check git version in macos": "git --version",
    "commit code in macos": "git commit -m 'message'",
}

random_facts = {
    # Science
    "what is the speed of light": "The speed of light is approximately 299,792 kilometers per second (km/s).",
    "what is the chemical symbol for water": "The chemical symbol for water is H2O.",
    "how many planets are in the solar system": "There are 8 planets in the solar system.",
    "what gas do plants absorb": "Plants absorb carbon dioxide (CO2).",
    "what is the boiling point of water": "The boiling point of water is 100°C (212°F) at sea level.",
    "what is the human body's largest organ": "The skin is the largest organ of the human body.",
    "what planet is known as the red planet": "Mars is known as the red planet.",
    "how many bones are in the adult human body": "There are 206 bones in the adult human body.",
    "what is the powerhouse of the cell": "The mitochondrion is the powerhouse of the cell.",
    "what is the most abundant gas in the earth's atmosphere": "Nitrogen makes up about 78% of the Earth's atmosphere.",
    "what force keeps us on the ground": "Gravity keeps us on the ground.",
    "what is the chemical formula for table salt": "Table salt is NaCl (sodium chloride).",
    "what part of the plant conducts photosynthesis": "The leaves conduct photosynthesis.",
    "how many chambers does the human heart have": "The human heart has 4 chambers.",
    "what is the center of an atom called": "The nucleus is the center of an atom.",
    "what is the unit of electric current": "The unit of electric current is the ampere (A).",
    "what planet has the most moons": "Saturn has the most moons (82 confirmed).",
    "what element does 'O' represent on the periodic table": "Oxygen.",
    "what gas do humans breathe in": "Humans breathe in oxygen.",
    "what is the freezing point of water": "0°C (32°F).",
    "which vitamin is produced when a person is exposed to sunlight": "Vitamin D.",
    "what is the main gas found in natural gas": "Methane (CH4).",
    "what is the pH of pure water": "7 (neutral).",
    "what organ is responsible for filtering blood": "The kidneys.",
    "what is the chemical symbol for gold": "Au.",
    "what is the process by which plants make food": "Photosynthesis.",
    "which planet is closest to the sun": "Mercury.",
    "what is the speed of sound": "Approximately 343 meters per second in air at room temperature.",
    "what kind of energy comes from the sun": "Solar energy.",
    "what is the smallest unit of life": "The cell.",
    "what type of animal is a frog": "Amphibian.",
    "what is the largest mammal": "The blue whale.",
    "what organ pumps blood throughout the body": "The heart.",
    "what gas do animals exhale": "Carbon dioxide.",
    "what is the name of the galaxy we live in": "The Milky Way.",
    "what is DNA": "Deoxyribonucleic acid, which carries genetic information.",
    "what is the hardest natural substance on Earth": "Diamond.",
    "what vitamin helps with blood clotting": "Vitamin K.",
    "what is a baby kangaroo called": "A joey.",
    "what is the process of water turning into vapor": "Evaporation.",
    "what planet is famous for its rings": "Saturn.",
    "how many teeth does an adult human have": "32.",
    "what part of the eye controls the amount of light entering": "The iris.",
    "what is the largest internal organ in the human body": "The liver.",
    "what type of blood cells fight infection": "White blood cells.",
    "what is the common name for sodium bicarbonate": "Baking soda.",
    "what element is essential for respiration": "Oxygen.",
    "what is the main function of red blood cells": "To carry oxygen.",
    "what is the formula for calculating speed": "Speed = Distance / Time.",
    "what kind of bond involves sharing electrons": "Covalent bond.",
    "what is the main gas involved in the greenhouse effect": "Carbon dioxide.",
    "what is the largest planet in our solar system": "Jupiter.",
    "what is the process where plants release water vapor": "Transpiration.",
    "which organ in humans produces insulin": "The pancreas.",
    "what does DNA stand for": "Deoxyribonucleic Acid.",
    "what is the term for animals that eat plants": "Herbivores.",
    "what is the study of living organisms called": "Biology.",
    "what is the freezing point of mercury": "-38.83°C.",
    "what is the common name for dihydrogen monoxide": "Water.",
    "what is the center of the Earth called": "The core.",
    "what is a scientist who studies rocks called": "A geologist.",
    "what gas do fire need to burn": "Oxygen.",
    "what is the process of converting solid to gas called": "Sublimation.",
    "what is the lightest element": "Hydrogen.",
    "which organ controls body temperature": "The hypothalamus.",
    "what is the main source of energy for Earth": "The Sun.",
    "what causes tides on Earth": "The moon's gravity.",
    "what is the largest species of shark": "The whale shark.",
    "how many teeth does a shark have": "Between 50 and 300 depending on the species.",
    "what is the function of the roots of a plant": "To absorb water and nutrients.",
    "which planet spins the fastest": "Jupiter.",
    "how many bones does a shark have": "None; sharks have cartilage instead of bones.",
    "what do bees collect from flowers": "Nectar.",
    "what is the chemical symbol for iron": "Fe.",
    "what is the name of the process by which plants lose water": "Transpiration.",
    "what is the name of the first artificial satellite": "Sputnik 1.",
    "who proposed the theory of relativity": "Albert Einstein.",
    "what is the normal body temperature of a human": "Approximately 37°C (98.6°F).",
    "what do you call molten rock after it erupts from a volcano": "Lava.",
    "what is the process by which cells divide": "Mitosis.",
    "what organ in the body produces bile": "The liver.",
    "what is the natural satellite of Earth": "The Moon.",
    "what is the term for animals that eat both plants and meat": "Omnivores.",
    "what is the freezing point of alcohol": "-114°C.",
    "what is the largest desert in the world": "The Sahara Desert.",
    "what is the process of a caterpillar turning into a butterfly": "Metamorphosis.",
    "what planet is known for its giant red spot": "Jupiter.",
    "what does a thermometer measure": "Temperature.",
    "what is the main function of the lungs": "To exchange oxygen and carbon dioxide.",
    "what is the name of the layer of air surrounding Earth": "The atmosphere.",
    "what organ in the human body produces insulin": "The pancreas.",
    # Geography
    "what is the capital of france": "Paris is the capital of France.",
    "which is the largest continent": "Asia is the largest continent by both area and population.",
    "what is the longest river in the world": "The Nile River is the longest river in the world.",
    "which country has the largest population": "China has the largest population.",
    "what is the smallest country in the world": "Vatican City is the smallest country.",
    "which desert is the hottest in the world": "The Sahara Desert is the hottest desert.",
    "what is the highest mountain in the world": "Mount Everest is the highest mountain.",
    "which ocean is the deepest": "The Pacific Ocean is the deepest ocean.",
    "what country is known as the land of the rising sun": "Japan is known as the land of the rising sun.",
    "what is the capital of australia": "Canberra is the capital of Australia.",
    "which river flows through egypt": "The Nile River flows through Egypt.",
    "what is the largest island in the world": "Greenland is the largest island.",
    "what is the capital of india": "New Delhi is the capital of India.",
    "which country has the most natural lakes": "Canada has the most natural lakes.",
    "what is the largest lake in the world": "The Caspian Sea is the largest lake.",
    "which continent is the driest": "Antarctica is the driest continent.",
    "what is the currency of japan": "The Japanese Yen (JPY) is the currency.",
    "what is the capital of canada": "Ottawa is the capital of Canada.",
    "which mountain range is the longest": "The Andes Mountains are the longest mountain range.",
    "what country has the most volcanoes": "Indonesia has the most active volcanoes.",
    "what is the largest country by area": "Russia is the largest country by area.",
    "which country is known as the land of the midnight sun": "Norway.",
    "what is the capital of brazil": "Brasília is the capital of Brazil.",
    "which country is famous for the Great Barrier Reef": "Australia.",
    "what is the smallest continent": "Australia.",
    "which city is known as the Big Apple": "New York City.",
    "what is the capital of south africa": "South Africa has three capitals: Pretoria (executive), Bloemfontein (judicial), and Cape Town (legislative).",
    "which ocean is the largest": "The Pacific Ocean.",
    "what is the capital of russia": "Moscow.",
    "which country is famous for the Eiffel Tower": "France.",
    "which continent is known as the Dark Continent": "Africa.",
    "what is the capital of egypt": "Cairo.",
    "which country is the largest producer of coffee": "Brazil.",
    "what is the capital of germany": "Berlin.",
    "which desert is the largest in the world": "The Sahara Desert.",
    "what country is home to the kangaroo": "Australia.",
    "what is the capital of italy": "Rome.",
    "which country has the most UNESCO World Heritage Sites": "Italy.",
    "what is the tallest building in the world": "Burj Khalifa in Dubai.",
    "which country has the largest rainforest": "Brazil (Amazon Rainforest).",
    "what is the capital of china": "Beijing.",
    "which country is known as the land of volcanoes": "Iceland.",
    "what is the capital of mexico": "Mexico City.",
    "which country is the largest exporter of oil": "Saudi Arabia.",
    "what is the capital of argentina": "Buenos Aires.",
    "which country is famous for the tulip fields": "The Netherlands.",
    "what is the capital of turkey": "Ankara.",
    "which continent has the most countries": "Africa.",
    "what is the capital of thailand": "Bangkok.",
    "which country is famous for the Great Wall": "China.",
    "what is the capital of united kingdom": "London.",
    "which country is known for its maple syrup": "Canada.",
    "what is the capital of indonesia": "Jakarta.",
    "which country has the longest coastline": "Canada.",
    "what is the capital of new zealand": "Wellington.",
    "which country is the largest in africa": "Algeria.",
    "what is the capital of greece": "Athens.",
    "which country is home to the Taj Mahal": "India.",
    "what is the capital of portugal": "Lisbon.",
    "which country is known for the samba dance": "Brazil.",
    "what is the capital of ireland": "Dublin.",
    "which country is famous for chocolate and watches": "Switzerland.",
    "what is the capital of norway": "Oslo.",
    "which country is home to the kangaroo": "Australia.",
    "what is the capital of south korea": "Seoul.",
    "which country is the birthplace of pizza": "Italy.",
    "what is the capital of belgium": "Brussels.",
    "which country is known as the Land of Fire and Ice": "Iceland.",
    "what is the capital of vietnam": "Hanoi.",
    "which country is famous for its fjords": "Norway.",
    "what is the capital of poland": "Warsaw.",
    "which country invented paper": "China.",
    "what is the capital of sweden": "Stockholm.",
    "which country is famous for Bollywood movies": "India.",
    "what is the capital of finland": "Helsinki.",
    "which country is home to the Colosseum": "Italy.",
    "what is the capital of denmark": "Copenhagen.",
    "which country is known for its ancient pyramids": "Egypt.",
    "what is the capital of hungary": "Budapest.",
    "which country is famous for Oktoberfest": "Germany.",
    "what is the capital of the netherlands": "Amsterdam.",
    "which country has the most volcanoes in europe": "Italy.",
    "what is the capital of austria": "Vienna.",
    "which country is known as the Emerald Isle": "Ireland.",
    "what is the capital of croatia": "Zagreb.",
    "which country is home to Machu Picchu": "Peru.",
    "what is the capital of czech republic": "Prague.",
    "which country is famous for its fjords": "Norway.",
    "what is the capital of slovakia": "Bratislava.",
    "which country has the oldest parliament": "Iceland.",
    # Science
    "what is the chemical symbol for water": "H2O is the chemical formula for water.",
    "who developed the theory of relativity": "Albert Einstein developed the theory of relativity.",
    "what planet is known as the red planet": "Mars is known as the red planet.",
    "what is the speed of light": "The speed of light is approximately 299,792 kilometers per second (km/s).",
    "what is the largest planet in our solar system": "Jupiter is the largest planet in our solar system.",
    "what gas do plants absorb from the atmosphere": "Plants absorb carbon dioxide (CO2).",
    "what is the basic unit of life": "The cell is the basic unit of life.",
    "who is known as the father of modern physics": "Galileo Galilei is often called the father of modern physics.",
    "what is the hardest natural substance": "Diamond is the hardest natural substance.",
    "what is the process by which plants make their food": "Photosynthesis.",
    "what is the powerhouse of the cell": "The mitochondrion is known as the powerhouse of the cell.",
    "what gas do humans breathe in": "Humans breathe in oxygen (O2).",
    "what is the boiling point of water": "100 degrees Celsius (212 degrees Fahrenheit) at sea level.",
    "what is the chemical symbol for gold": "Au is the chemical symbol for gold.",
    "who discovered penicillin": "Alexander Fleming discovered penicillin.",
    "what is the atomic number of carbon": "6.",
    "which planet has rings around it": "Saturn.",
    "what force keeps us on the ground": "Gravity.",
    "what is the smallest particle of an element": "An atom.",
    "who formulated the laws of motion": "Isaac Newton.",
    "what is the chemical symbol for sodium": "Na.",
    "what is the process of cell division called": "Mitosis.",
    "what vitamin is produced when a person is exposed to sunlight": "Vitamin D.",
    "which organ is responsible for pumping blood": "The heart.",
    "what is the main gas found in the air we breathe": "Nitrogen (about 78%).",
    "who is known for the theory of evolution": "Charles Darwin.",
    "what is the speed of sound": "Approximately 343 meters per second in air at sea level.",
    "what is the pH value of pure water": "7 (neutral).",
    "which element has the highest melting point": "Tungsten.",
    "what is the chemical symbol for iron": "Fe.",
    "what type of bond holds water molecules together": "Hydrogen bonds.",
    "who discovered electricity": "Benjamin Franklin contributed to understanding electricity.",
    "what is the process by which water changes from liquid to gas": "Evaporation.",
    "which organ is responsible for filtering blood": "The kidneys.",
    "what is the most abundant element in the universe": "Hydrogen.",
    "what is the chemical formula for table salt": "NaCl (sodium chloride).",
    "who invented the telephone": "Alexander Graham Bell.",
    "what is the largest organ in the human body": "The skin.",
    "what type of animal is a frog": "An amphibian.",
    "what is the freezing point of water": "0 degrees Celsius (32 degrees Fahrenheit).",
    "what part of the plant conducts photosynthesis": "Leaves.",
    "which scientist is famous for his work on radioactivity": "Marie Curie.",
    "what is the chemical symbol for helium": "He.",
    "what is the process of breathing called": "Respiration.",
    "which planet is closest to the sun": "Mercury.",
    "what is the function of red blood cells": "To carry oxygen.",
    "what is the chemical formula for carbon dioxide": "CO2.",
    "what is the largest mammal": "The blue whale.",
    "what is the name of our galaxy": "The Milky Way.",
    "who discovered gravity": "Isaac Newton formulated the law of gravity.",
    "what is the smallest bone in the human body": "The stapes bone in the ear.",
    "what is the human body's largest artery": "The aorta.",
    "what is DNA": "Deoxyribonucleic acid, the molecule that carries genetic information.",
    "what is the chemical symbol for oxygen": "O.",
    "who invented the light bulb": "Thomas Edison is credited with inventing the practical light bulb.",
    "what part of the cell contains genetic material": "The nucleus.",
    "what type of energy is stored in food": "Chemical energy.",
    "what is the basic unit of heredity": "The gene.",
    "what is the main function of white blood cells": "To fight infection.",
    "what is the chemical formula for methane": "CH4.",
    "which organ produces insulin": "The pancreas.",
    "what is the name of the process by which plants release oxygen": "Photosynthesis.",
    "what type of rock is formed from cooled lava": "Igneous rock.",
    "who developed the periodic table": "Dmitri Mendeleev.",
    "what is the chemical symbol for potassium": "K.",
    "what is the center of an atom called": "The nucleus.",
    "what type of energy is produced by the sun": "Solar energy.",
    "what is the main gas responsible for global warming": "Carbon dioxide (CO2).",
    "which part of the eye controls the amount of light entering": "The iris.",
    "what is the term for animals that eat only plants": "Herbivores.",
    "what is the basic unit of a chemical element": "An atom.",
    "who discovered radio waves": "Heinrich Hertz.",
    "what is the largest planet in the solar system": "Jupiter.",
    "what is the name of the process where plants make food": "Photosynthesis.",
    "which element is needed for respiration": "Oxygen.",
    "what is the term for animals that eat meat": "Carnivores.",
    "what is the name of the force that opposes motion": "Friction.",
    "who is known for the laws of planetary motion": "Johannes Kepler.",
    "what is the name of the particle that orbits the nucleus": "Electron.",
    "what is the name of the gas used in balloons to make them float": "Helium.",
    "what is the chemical formula for ozone": "O3.",
    "who invented the airplane": "The Wright brothers.",
    "what is the name of the process where water changes from gas to liquid": "Condensation.",
    "what is the name of the scientist who discovered radioactivity": "Henri Becquerel.",
    "what is the value of pi": "Pi (π) is approximately 3.14159.",
    "what is the formula for the area of a circle": "Area = π * radius².",
    "what is the formula for the circumference of a circle": "Circumference = 2 * π * radius.",
    "what is the pythagorean theorem": "In a right triangle, a² + b² = c².",
    "what is a prime number": "A prime number is a number greater than 1 with only two factors: 1 and itself.",
    "what is the quadratic formula": "x = [-b ± √(b² - 4ac)] / (2a).",
    "what is the sum of angles in a triangle": "The sum of angles in a triangle is 180 degrees.",
    "what is the fibonacci sequence": "A sequence where each number is the sum of the two preceding ones, starting with 0 and 1.",
    "what is the factorial of a number": "Factorial of n (n!) is the product of all positive integers up to n.",
    "what is an irrational number": "A number that cannot be expressed as a simple fraction and has infinite non-repeating decimals.",
    "what is the golden ratio": "Approximately 1.618, it appears in many natural patterns and designs.",
    "what is the formula for the area of a rectangle": "Area = length * width.",
    "what is the volume of a cube": "Volume = side³.",
    "what is the slope of a line": "Slope = rise/run = change in y divided by change in x.",
    "what is the difference between permutation and combination": "Permutation considers order; combination does not.",
    "what is the sum of interior angles of a polygon": "Sum = (n-2) * 180 degrees, where n is number of sides.",
    "what is the formula for the volume of a cylinder": "Volume = π * radius² * height.",
    "what is the discriminant in quadratic equations": "Discriminant = b² - 4ac; determines the nature of roots.",
    "what is a rational number": "A number that can be expressed as a fraction of two integers.",
    "what is the formula for the area of a triangle": "Area = 1/2 * base * height.",
    "what is a prime factorization": "Expressing a number as a product of prime numbers.",
    "what is a polynomial": "An expression consisting of variables and coefficients combined using addition, subtraction, multiplication, and non-negative integer exponents.",
    "what is the law of sines": "sin A / a = sin B / b = sin C / c for a triangle.",
    "what is the law of cosines": "c² = a² + b² - 2ab cos C.",
    "what is the binomial theorem": "Describes the algebraic expansion of powers of a binomial.",
    "what is an asymptote": "A line a graph approaches but never touches.",
    "what is the difference between mean, median, and mode": "Mean is average, median is middle value, mode is most frequent value.",
    "what is a function": "A relation where each input has exactly one output.",
    "what is a linear equation": "An equation that makes a straight line when graphed.",
    "what is the Pythagorean triple": "A set of three integers (a,b,c) satisfying a² + b² = c².",
    "what is an angle": "The figure formed by two rays sharing a common endpoint.",
    "what is the formula for the surface area of a sphere": "Surface area = 4π * radius².",
    "what is the formula for the volume of a sphere": "Volume = 4/3 * π * radius³.",
    "what is a vector": "A quantity having both magnitude and direction.",
    "what is the difference between a scalar and a vector": "Scalars have magnitude only; vectors have magnitude and direction.",
    "what is the principle of mathematical induction": "A method to prove statements for all natural numbers.",
    "what is the coordinate plane": "A plane with a horizontal x-axis and vertical y-axis used to plot points.",
    "what is the distributive property": "a(b + c) = ab + ac.",
    "what is an equation": "A mathematical statement that asserts equality of two expressions.",
    "what is an inequality": "A mathematical statement that compares two expressions using >, <, ≥, or ≤.",
    "what is the factorial of 0": "0! = 1 by definition.",
    "what is a prime number between 1 and 10": "2, 3, 5, and 7.",
    "what is the formula for the perimeter of a rectangle": "Perimeter = 2 * (length + width).",
    "what is the difference between area and perimeter": "Area measures space inside; perimeter measures distance around.",
    "what is the formula for distance between two points": "Distance = √[(x2 - x1)² + (y2 - y1)²].",
    "what is an acute angle": "An angle less than 90 degrees.",
    "what is an obtuse angle": "An angle greater than 90 degrees but less than 180 degrees.",
    "what is a right angle": "An angle exactly 90 degrees.",
    "what is the sum of exterior angles of any polygon": "360 degrees.",
    "what is a circle": "A set of points equidistant from a center point.",
    "what is the median of a data set": "The middle value when data is ordered.",
    "what is the mode of a data set": "The value that appears most frequently.",
    "what is a histogram": "A graphical representation of data using bars.",
    "what is a probability": "A measure of the likelihood of an event occurring.",
    "what is the formula for simple interest": "I = P * r * t, where I is interest, P is principal, r is rate, and t is time.",
    "what is the Pythagorean theorem used for": "To find the length of sides in a right triangle.",
    "what is a circle's radius": "Distance from center to any point on the circle.",
    "what is a circle's diameter": "Distance across the circle through the center; diameter = 2 * radius.",
    "what is an angle bisector": "A line that divides an angle into two equal parts.",
    "what is an equation of a line": "y = mx + b, where m is slope and b is y-intercept.",
    "what is the formula for compound interest": "A = P(1 + r/n)^(nt).",
    "what is an integer": "A whole number, positive, negative, or zero.",
    "what is the distributive law used for": "To multiply a single term over terms inside parentheses.",
    "what is the zero property of multiplication": "Any number multiplied by zero is zero.",
    "what is the commutative property": "a + b = b + a or ab = ba.",
    "what is the associative property": "(a + b) + c = a + (b + c).",
    "what is a ratio": "A comparison of two quantities by division.",
    "what is a proportion": "An equation that states two ratios are equal.",
    "what is a polygon": "A closed figure with straight sides.",
    "what is a parallelogram": "A quadrilateral with opposite sides parallel.",
    "what is a trapezoid": "A quadrilateral with exactly one pair of parallel sides.",
    "what is a rhombus": "A parallelogram with all sides equal length.",
    "what is the area of a parallelogram": "Base * height.",
    "what is the Pythagorean theorem formula": "a² + b² = c².",
    "what is a congruent shape": "Shapes that are identical in size and shape.",
    "what is similar shape": "Shapes with the same shape but different sizes.",
    "what is the volume of a rectangular prism": "Length * width * height.",
    "what is a square number": "A number that is the product of an integer multiplied by itself.",
    "what is a composite number": "A number that has more than two factors.",
    "what is the formula for the surface area of a cube": "6 * side².",
    "what is a coefficient": "A numerical or constant factor in a term of an algebraic expression.",
    "what is the least common multiple (LCM)": "The smallest number divisible by two or more numbers.",
    "what is the greatest common divisor (GCD)": "The largest number dividing two or more numbers without remainder.",
    "what is an absolute value": "The distance of a number from zero on the number line.",
    "what is the formula for slope": "(y2 - y1) / (x2 - x1).",
    "what is a histogram": "A bar graph representing frequency distribution.",
    "what is a function domain": "All possible input values (x-values) for a function.",
    "what is a function range": "All possible output values (y-values) for a function.",
    "what is the bermuda triangle": "A region in the North Atlantic where ships and planes are said to mysteriously disappear.",
    "what is crop circle": "Patterns mysteriously appearing overnight in fields, often attributed to aliens or unknown forces.",
    "what is the mystery of the lost city of atlantis": "A legendary advanced civilization said to have sunk into the ocean.",
    "what is the mystery behind the pyramids": "How ancient Egyptians built the pyramids with precise alignment and massive stones remains partly unexplained.",
    "what is the wow signal": "A brief, unexplained radio signal from space detected in 1977, possibly from extraterrestrial origin.",
    "what is the mystery of stonehenge": "A prehistoric monument in England with unclear purposes, possibly related to astronomy or rituals.",
    "what is the taos hum": "A low-frequency humming noise heard by some residents of Taos, New Mexico, with no identified source.",
    "what is the mystery of the siberian tigers": "Some Siberian tigers are said to mysteriously vanish without trace in their habitat.",
    "what is the mystery of the lost roman legion": "The disappearance of the Roman Ninth Legion in Britain remains unresolved.",
    "what is the mystery of roanoke island": "The entire colony vanished mysteriously in the late 1500s with only the word 'Croatoan' left behind.",
    "what is the mystery of the zodiac killer": "An unidentified serial killer who taunted police with cryptic messages in the 1960s-70s.",
    "what is the mystery of the moai statues": "Massive stone statues on Easter Island whose construction and transportation methods are debated.",
    "what is the mystery of the mary celeste": "An abandoned ship found drifting with no crew and no clear explanation.",
    "what is the mystery of the crystal skulls": "Carved skulls made from clear quartz with disputed origins and alleged supernatural powers.",
    "what is the mystery of the chupacabra": "A legendary creature reported to attack livestock in Latin America, origin unknown.",
    "what is the mystery of the green children of woolpit": "Medieval legend of two green-skinned children appearing in a village in England.",
    "what is the mystery of the taured man": "A man allegedly arrived at an airport from a country that doesn't exist and then vanished.",
    "what is the mystery of the dancing plague": "A medieval phenomenon where groups danced uncontrollably for days.",
    "what is the mystery of the humming pyramids": "Some pyramids allegedly emit unexplained sounds or vibrations.",
    "what is the mystery of the medusa effect": "Stories of people turning to stone or statues mysteriously cracking near Medusa imagery.",
    "what is the mystery of the sumerian king list": "Ancient document listing kings with impossibly long reigns, suggesting lost knowledge.",
    "what is the mystery of the ancient aliens": "Theory that extraterrestrials influenced ancient human civilizations.",
    "what is the mystery of the fermi paradox": "The contradiction between high probability of extraterrestrial life and lack of evidence.",
    "what is the mystery of the ogham stones": "Ancient stones with undeciphered inscriptions found in Ireland.",
    "what is the mystery of the narwhal tusk": "Often called the unicorn of the sea, narwhal tusks have fascinated cultures.",
    "what is the mystery of the amazon rainforest lights": "Unexplained lights often seen above the Amazon at night.",
    "what is the mystery of the jack the ripper": "An unidentified serial killer active in London in 1888.",
    "what is the mystery of the sarcophagus curse": "Belief that disturbing ancient Egyptian tombs triggers curses.",
    "what is the mystery of the antimatter in the universe": "Why there is more matter than antimatter is an unsolved question.",
    "what is the mystery of the double sunset": "Rare phenomenon where the sun appears to set twice in a short time at some locations.",
    "what is the mystery of the basque language": "A European language isolate with no known relatives or origins.",
    "what is the mystery of the moai eye sockets": "Whether the statues' eye sockets were ever filled or symbolized something unknown.",
    "what is the mystery of the black eyed children": "Urban legends of children with solid black eyes appearing mysteriously.",
    "what is the mystery of the bee decline": "Global mysterious decline of bee populations affecting ecosystems.",
    "what is the mystery of the hummingbird migration": "Long migration routes that challenge scientific understanding.",
    "what is the mystery of the ghost ships": "Abandoned vessels found at sea with no explanation of crew disappearance.",
    "what is the mystery of the bas-relief": "Ancient carved stones with unclear symbolic meanings.",
    "what is the mystery of the ancient maps": "Maps showing lands or coastlines unknown at their time of creation.",
    "what is the mystery of the titanic sinking": "Questions remain about the exact causes and conspiracy theories.",
    "what is the mystery of the sargasso sea": "A region in the Atlantic Ocean known for strange currents and debris.",
    "what is the mystery of the moon landing conspiracy": "Claims that the 1969 moon landing was faked, despite evidence.",
    "what is the mystery of the anunnaki": "Ancient Sumerian gods believed by some to be extraterrestrials.",
    "what is the mystery of the dendera light": "Ancient Egyptian carvings some interpret as depicting electrical lighting.",
    "what is the mystery of the nazca lines": "Massive geoglyphs in Peru with unknown purpose and creation method.",
    "what is the mystery of the vinland map": "A map purportedly showing Viking discovery of America before Columbus.",
    "what is the mystery of the gobekli tepe": "A 12,000-year-old archaeological site predating known civilizations.",
    "what is the mystery of the dead sea scrolls": "Ancient texts discovered with unknown authorship and secret content.",
    "what is the mystery of the taured passport": "A passport from a non-existent country found on a mysterious traveler.",
    "what is the mystery of the dancing lights of norway": "Northern lights with strange shapes and colors defying explanation.",
    "what is the mystery of the hanging gardens": "Ancient wonder whose existence and location remain unconfirmed.",
    "what is the mystery of the ziggurats": "Step pyramids with unknown full purpose and construction methods.",
    "what is the mystery of the mayan calendar": "An advanced calendar predicting astronomical events and cycles.",
    "what is the mystery of the ancient sundial": "Early timekeeping devices whose precision amazed historians.",
    "what is the mystery of the crystal cave": "A natural cave filled with enormous quartz crystals.",
    "what is the mystery of the black hole information paradox": "Unresolved conflict about information preservation in black holes.",
    "what is the mystery of the spontaneous human combustion": "Cases of people mysteriously burning without an external source.",
    "what is the mystery of the ricin poisonings": "Rare poisonings involving the deadly ricin toxin with unknown perpetrators.",
    "what is the mystery of the mokele-mbembe": "A cryptid rumored to live in the Congo resembling a dinosaur.",
    "what is the mystery of the 1908 tunguska event": "A massive explosion in Siberia with unclear origin, possibly a meteor.",
    "what is the mystery of the polybius arcade game": "An urban legend about a game causing strange psychological effects.",
    "what is the mystery of the ancient stone spheres": "Large perfectly round spheres found in Costa Rica with unknown purpose.",
    "what is the mystery of the green children": "Children with green skin who appeared mysteriously in medieval England.",
    "what is the mystery of the los angeles earthquake lights": "Strange luminous phenomena before or during earthquakes.",
    "what is the mystery of the phantom time hypothesis": "Theory that 300 years of history were fabricated in the Middle Ages.",
    "what is the mystery of the lost continent of mu": "Legend of a sunken continent in the Pacific Ocean.",
    "what is the mystery of the riddle of the sphinx": "Ancient Egyptian riddle associated with the Sphinx statue.",
    "what is the mystery of the ekaterinburg meteorite": "Unusual meteorite fragments with strange chemical composition.",
    "what is the mystery of the ball lightning": "Rare unexplained phenomenon of glowing spheres during thunderstorms.",
    "what is the mystery of the singing sand dunes": "Some sand dunes emit musical sounds when wind blows.",
    "what is the mystery of the black knight satellite": "A supposed alien satellite orbiting Earth in conspiracy theories.",
    "what is the mystery of the romulan star system": "Fictional but inspired real searches for unknown star systems.",
    "what is the mystery of the tabby star": "A star with strange dimming patterns possibly caused by alien megastructures.",
    "what is the mystery of the lost treasure of the pirates": "Legends of hidden pirate gold buried in secret locations.",
    "what is the mystery of the oak island money pit": "A shaft with buried treasure and booby traps on Oak Island, Canada.",
    "what is the mystery of the black forest": "German forest associated with myths, witches, and supernatural tales.",
    "what is the mystery of the green flash": "A rare optical phenomenon seen just after sunset or before sunrise.",
    "what is the mystery of the zodiacs symbols": "Ancient symbols representing constellations with hidden meanings.",
    "what is the mystery of the men in black": "Alleged mysterious agents who suppress UFO information.",
    "what is the mystery of the phoenix lights": "Mass UFO sighting in Arizona in 1997 with unexplained lights.",
    "what is the mystery of the giza plateau": "Complex of pyramids and temples with many unanswered questions.",
    "what is the mystery of the great wall of china": "How it was built and its full original purpose debated.",
    "what is the mystery of the shroud of turin": "A linen cloth believed by some to bear Jesus's image.",
    "what is the mystery of the flying dutchman": "A ghost ship doomed to sail forever.",
    "what is the mystery of the ancient fossil": "Fossils found that challenge the known timeline of life on Earth.",
    "what is the mystery of the marfa lights": "Mysterious glowing orbs seen in Marfa, Texas.",
    "what is the mystery of the amber room": "A room made of amber panels that vanished during WWII.",
    "what is the mystery of the monster of loch ness": "A large aquatic creature reputed to live in Scotland's Loch Ness.",
    "what is the mystery of the pyramids alignment": "Precise alignment of pyramids with stars and cardinal points.",
    "what is the mystery of the ancient manuscript": "Unknown languages and codes in ancient documents still undeciphered.",
    "what is the mystery of the babushka lady": "An unidentified woman who filmed JFK assassination events.",
    "what is the mystery of the shadow people": "Entities seen as dark humanoid shapes in peripheral vision.",
    "what is the mystery of the mandela effect": "Collective false memories of events or facts.",
    "what is the mystery of the cryptic cave paintings": "Ancient paintings with unknown symbolism or meaning.",
    "what is the mystery of the great flood": "Stories of a worldwide flood found in many ancient cultures.",
    "what is the mystery of the disappeared colony": "Many early colonies vanished without a trace or explanation.",
    "what is the mystery of the black diamond": "Rare black diamonds with unusual origins and properties.",
    "what is the mystery of the crystal skulls": "Carved skulls with alleged mystical powers and mysterious origins."
}


mysql_queries = {
    # Create database
    "how do i create a database in mysql": "CREATE DATABASE database_name;",
    "command to create database in mysql": "CREATE DATABASE database_name;",
    "mysql create database": "CREATE DATABASE database_name;",
    "how to make a database in mysql": "CREATE DATABASE database_name;",
    "mysql command to create a database": "CREATE DATABASE database_name;",

    # Use database
    "how do i select a database in mysql": "USE database_name;",
    "mysql use database": "USE database_name;",
    "how to switch database in mysql": "USE database_name;",

    # Create table
    "how do i create a table in mysql": """CREATE TABLE table_name (
    column1 datatype,
    column2 datatype,
    column3 datatype,
    PRIMARY KEY (column1)
);""",
    "mysql create table": """CREATE TABLE table_name (
    column1 datatype,
    column2 datatype,
    column3 datatype,
    PRIMARY KEY (column1)
);""",

    # Show tables
    "how to show all tables in mysql": "SHOW TABLES;",
    "mysql show tables": "SHOW TABLES;",
    "command to list tables in mysql": "SHOW TABLES;",

    # Insert data
    "how do i insert data in mysql": "INSERT INTO table_name (column1, column2) VALUES (value1, value2);",
    "mysql insert query": "INSERT INTO table_name (column1, column2) VALUES (value1, value2);",
    "command to insert data in mysql": "INSERT INTO table_name (column1, column2) VALUES (value1, value2);",

    # Select data
    "how to select all data from a table in mysql": "SELECT * FROM table_name;",
    "mysql select all": "SELECT * FROM table_name;",
    "command to select all from mysql table": "SELECT * FROM table_name;",

    # Select specific columns
    "how to select specific columns in mysql": "SELECT column1, column2 FROM table_name;",
    "mysql select columns": "SELECT column1, column2 FROM table_name;",

    # Where clause
    "how to filter data in mysql": "SELECT * FROM table_name WHERE condition;",
    "mysql select with condition": "SELECT * FROM table_name WHERE condition;",

    # Update data
    "how do i update data in mysql": "UPDATE table_name SET column1 = value1 WHERE condition;",
    "mysql update query": "UPDATE table_name SET column1 = value1 WHERE condition;",

    # Delete data
    "how do i delete data in mysql": "DELETE FROM table_name WHERE condition;",
    "mysql delete query": "DELETE FROM table_name WHERE condition;",

    # Drop table
    "how to drop a table in mysql": "DROP TABLE table_name;",
    "mysql drop table": "DROP TABLE table_name;",

    # Alter table add column
    "how to add a column in mysql table": "ALTER TABLE table_name ADD column_name datatype;",
    "mysql add column": "ALTER TABLE table_name ADD column_name datatype;",

    # Alter table drop column
    "how to remove a column from mysql table": "ALTER TABLE table_name DROP COLUMN column_name;",
    "mysql drop column": "ALTER TABLE table_name DROP COLUMN column_name;",

    # Create index
    "how to create an index in mysql": "CREATE INDEX index_name ON table_name (column_name);",
    "mysql create index": "CREATE INDEX index_name ON table_name (column_name);",

    # Join tables
    "how to join two tables in mysql": """SELECT columns
FROM table1
JOIN table2 ON table1.column = table2.column;""",
    "mysql join query": """SELECT columns
FROM table1
JOIN table2 ON table1.column = table2.column;""",

    # Group by
    "how to group data in mysql": "SELECT column, COUNT(*) FROM table_name GROUP BY column;",
    "mysql group by": "SELECT column, COUNT(*) FROM table_name GROUP BY column;",

    # Order by
    "how to order data in mysql": "SELECT * FROM table_name ORDER BY column ASC|DESC;",
    "mysql order by": "SELECT * FROM table_name ORDER BY column ASC|DESC;",

    # Limit results
    "how to limit query results in mysql": "SELECT * FROM table_name LIMIT number;",
    "mysql limit": "SELECT * FROM table_name LIMIT number;",

    # Like operator
    "how to use like operator in mysql": "SELECT * FROM table_name WHERE column LIKE '%pattern%';",
    "mysql like query": "SELECT * FROM table_name WHERE column LIKE '%pattern%';",

    # Distinct
    "how to select distinct values in mysql": "SELECT DISTINCT column FROM table_name;",
    "mysql distinct": "SELECT DISTINCT column FROM table_name;",

    # Aggregate functions
    "how to count rows in mysql": "SELECT COUNT(*) FROM table_name;",
    "mysql count function": "SELECT COUNT(*) FROM table_name;",
    "how to get max value in mysql": "SELECT MAX(column) FROM table_name;",
    "mysql max function": "SELECT MAX(column) FROM table_name;",
    "how to get min value in mysql": "SELECT MIN(column) FROM table_name;",
    "mysql min function": "SELECT MIN(column) FROM table_name;",
    "how to get average in mysql": "SELECT AVG(column) FROM table_name;",
    "mysql avg function": "SELECT AVG(column) FROM table_name;",
    "how to sum column values in mysql": "SELECT SUM(column) FROM table_name;",
    "mysql sum function": "SELECT SUM(column) FROM table_name;",

    # Describe table
    "how to describe a table in mysql": "DESCRIBE table_name;",
    "mysql describe table": "DESCRIBE table_name;",

    # Show databases
    "how to show all databases in mysql": "SHOW DATABASES;",
    "mysql show databases": "SHOW DATABASES;",

    # Foreign key
    "how to add foreign key in mysql": """ALTER TABLE child_table
ADD CONSTRAINT fk_name FOREIGN KEY (column_name)
REFERENCES parent_table(column_name);""",
    "mysql add foreign key": """ALTER TABLE child_table
ADD CONSTRAINT fk_name FOREIGN KEY (column_name)
REFERENCES parent_table(column_name);""",

    # Transactions
    "how to start a transaction in mysql": "START TRANSACTION;",
    "mysql start transaction": "START TRANSACTION;",
    "how to commit transaction in mysql": "COMMIT;",
    "mysql commit": "COMMIT;",
    "how to rollback transaction in mysql": "ROLLBACK;",
    "mysql rollback": "ROLLBACK;",

    # Show create table
    "how to see create table statement in mysql": "SHOW CREATE TABLE table_name;",
    "mysql show create table": "SHOW CREATE TABLE table_name;",

    # Rename table
    "how to rename a table in mysql": "RENAME TABLE old_name TO new_name;",
    "mysql rename table": "RENAME TABLE old_name TO new_name;",

    # Truncate table
    "how to truncate table in mysql": "TRUNCATE TABLE table_name;",
    "mysql truncate table": "TRUNCATE TABLE table_name;",

    # Explain query
    "how to explain query in mysql": "EXPLAIN SELECT * FROM table_name;",
    "mysql explain": "EXPLAIN SELECT * FROM table_name;",

    # Create user
    "how to create user in mysql": "CREATE USER 'username'@'host' IDENTIFIED BY 'password';",
    "mysql create user": "CREATE USER 'username'@'host' IDENTIFIED BY 'password';",

    # Grant privileges
    "how to grant privileges in mysql": "GRANT ALL PRIVILEGES ON database_name.* TO 'username'@'host';",
    "mysql grant privileges": "GRANT ALL PRIVILEGES ON database_name.* TO 'username'@'host';",

    # Revoke privileges
    "how to revoke privileges in mysql": "REVOKE ALL PRIVILEGES ON database_name.* FROM 'username'@'host';",
    "mysql revoke privileges": "REVOKE ALL PRIVILEGES ON database_name.* FROM 'username'@'host';",

    # Drop user
    "how to drop user in mysql": "DROP USER 'username'@'host';",
    "mysql drop user": "DROP USER 'username'@'host';",
}

github_cmds = {
    # Initialize repository
    "how do i initialize a git repository": "git init",
    "how to create a new git repo": "git init",
    "git command to start repository": "git init",
    "initialize git repository": "git init",

    # Clone repository
    "how to clone a github repo": "git clone REPO_URL",
    "clone repository from github": "git clone REPO_URL",
    "git clone command": "git clone REPO_URL",
    "copy a git repository": "git clone REPO_URL",

    # Check status
    "how to check git status": "git status",
    "git status command": "git status",
    "show git status": "git status",

    # Add files
    "how to add files to git": "git add FILE_NAME",
    "git add command": "git add FILE_NAME",
    "stage files for commit": "git add FILE_NAME",
    "add file to git staging area": "git add FILE_NAME",
    "add all files to git": "git add .",
    "stage all files": "git add .",

    # Commit changes
    "how to commit changes in git": "git commit -m 'commit message'",
    "git commit command": "git commit -m 'commit message'",
    "save changes in git": "git commit -m 'commit message'",
    "commit staged files": "git commit -m 'commit message'",

    # Push changes
    "how to push changes to github": "git push origin BRANCH_NAME",
    "git push command": "git push origin BRANCH_NAME",
    "upload local commits to remote": "git push origin BRANCH_NAME",

    # Pull changes
    "how to pull latest changes from github": "git pull origin BRANCH_NAME",
    "git pull command": "git pull origin BRANCH_NAME",
    "fetch and merge from remote": "git pull origin BRANCH_NAME",

    # Create branch
    "how to create a new branch in git": "git branch BRANCH_NAME",
    "git branch command": "git branch BRANCH_NAME",
    "make a new branch": "git branch BRANCH_NAME",

    # Switch branch
    "how to switch branches in git": "git checkout BRANCH_NAME",
    "git checkout command": "git checkout BRANCH_NAME",
    "change git branch": "git checkout BRANCH_NAME",

    # Create and switch branch
    "how to create and switch to a new branch": "git checkout -b BRANCH_NAME",
    "git create and switch branch": "git checkout -b BRANCH_NAME",

    # Merge branch
    "how to merge a branch in git": "git merge BRANCH_NAME",
    "git merge command": "git merge BRANCH_NAME",

    # Show commit log
    "how to see commit history": "git log",
    "git log command": "git log",
    "view git commit history": "git log",

    # Show remote info
    "how to show git remotes": "git remote -v",
    "list git remotes": "git remote -v",

    # Add remote
    "how to add a remote repository": "git remote add origin REPO_URL",
    "git add remote command": "git remote add origin REPO_URL",

    # Remove remote
    "how to remove a remote in git": "git remote remove origin",
    "git remove remote": "git remote remove origin",

    # Stash changes
    "how to stash changes in git": "git stash",
    "git stash command": "git stash",
    "save changes temporarily": "git stash",

    # Apply stash
    "how to apply stashed changes": "git stash apply",
    "git stash apply command": "git stash apply",

    # Drop stash
    "how to drop stash in git": "git stash drop",
    "git drop stash": "git stash drop",

    # Show stash list
    "how to list all stashes": "git stash list",
    "git stash list command": "git stash list",

    # Delete branch
    "how to delete a branch": "git branch -d BRANCH_NAME",
    "git delete branch": "git branch -d BRANCH_NAME",

    # Rename branch
    "how to rename current branch": "git branch -m NEW_BRANCH_NAME",
    "git rename branch": "git branch -m NEW_BRANCH_NAME",

    # Show differences
    "how to see changes": "git diff",
    "git diff command": "git diff",

    # Undo changes to file
    "how to undo changes to a file": "git checkout -- FILE_NAME",
    "discard changes in file": "git checkout -- FILE_NAME",

    # Reset staged files
    "how to unstage a file": "git reset HEAD FILE_NAME",
    "unstage file in git": "git reset HEAD FILE_NAME",

    # Show current branch
    "how to see current branch": "git branch --show-current",
    "git current branch": "git branch --show-current",

    # Fetch remote updates
    "how to fetch changes from remote": "git fetch",
    "git fetch command": "git fetch",

    # Rebase branch
    "how to rebase branch": "git rebase BRANCH_NAME",
    "git rebase command": "git rebase BRANCH_NAME",

    # Show file history
    "how to see history of a file": "git log -- FILE_NAME",
    "git log file history": "git log -- FILE_NAME",

    # Tag commit
    "how to create a tag": "git tag TAG_NAME",
    "git tag command": "git tag TAG_NAME",

    # Push tags
    "how to push tags to remote": "git push origin TAG_NAME",
    "git push tag": "git push origin TAG_NAME",
}

powershell_cmds = {
    # Create directory/folder
    "how do i make a directory in powershell": "New-Item -ItemType Directory -Path DIRECTORY_NAME",
    "how do i create a folder in powershell": "New-Item -ItemType Directory -Path DIRECTORY_NAME",
    "command to create directory in powershell": "New-Item -ItemType Directory -Path DIRECTORY_NAME",
    "make a directory powershell": "New-Item -ItemType Directory -Path DIRECTORY_NAME",
    "create folder powershell": "New-Item -ItemType Directory -Path DIRECTORY_NAME",
    "mkdir command powershell": "New-Item -ItemType Directory -Path DIRECTORY_NAME",
    "powershell create new directory": "New-Item -ItemType Directory -Path DIRECTORY_NAME",

    # Delete file or folder
    "how to delete a file in powershell": "Remove-Item FILE_NAME",
    "how do i remove a file in powershell": "Remove-Item FILE_NAME",
    "delete file powershell": "Remove-Item FILE_NAME",
    "remove file powershell": "Remove-Item FILE_NAME",
    "delete folder in powershell": "Remove-Item -Recurse DIRECTORY_NAME",
    "delete directory powershell": "Remove-Item -Recurse DIRECTORY_NAME",
    "remove directory powershell": "Remove-Item -Recurse DIRECTORY_NAME",
    "remove folder powershell": "Remove-Item -Recurse DIRECTORY_NAME",
    "rmdir command powershell": "Remove-Item -Recurse DIRECTORY_NAME",

    # Copy files
    "how to copy a file in powershell": "Copy-Item SOURCE DESTINATION",
    "copy file powershell": "Copy-Item SOURCE DESTINATION",
    "command to copy file in powershell": "Copy-Item SOURCE DESTINATION",
    "duplicate file powershell": "Copy-Item SOURCE DESTINATION",
    "powershell copy command": "Copy-Item SOURCE DESTINATION",

    # Move files
    "how to move a file in powershell": "Move-Item SOURCE DESTINATION",
    "move file powershell": "Move-Item SOURCE DESTINATION",
    "command to move file in powershell": "Move-Item SOURCE DESTINATION",
    "transfer file powershell": "Move-Item SOURCE DESTINATION",
    "powershell move command": "Move-Item SOURCE DESTINATION",

    # List directory contents
    "how to list files in powershell": "Get-ChildItem",
    "list directory powershell": "Get-ChildItem",
    "show files powershell": "Get-ChildItem",
    "dir command powershell": "Get-ChildItem",
    "list folder contents powershell": "Get-ChildItem",
    "get directory listing powershell": "Get-ChildItem",

    # Clear screen
    "how to clear the screen in powershell": "Clear-Host",
    "clear terminal powershell": "Clear-Host",
    "clear console powershell": "Clear-Host",
    "cls command powershell": "Clear-Host",

    # Show IP config
    "how to show ip address in powershell": "Get-NetIPAddress",
    "show ip config powershell": "Get-NetIPAddress",
    "ipconfig powershell": "Get-NetIPAddress",

    # Ping command
    "how to ping in powershell": "Test-Connection ADDRESS",
    "ping command powershell": "Test-Connection ADDRESS",
    "test connectivity powershell": "Test-Connection ADDRESS",
    "check network connection powershell": "Test-Connection ADDRESS",

    # Get process info
    "how to get running processes in powershell": "Get-Process",
    "list processes powershell": "Get-Process",
    "show running tasks powershell": "Get-Process",

    # Stop a process
    "how to stop a process in powershell": "Stop-Process -Name PROCESS_NAME",
    "kill process powershell": "Stop-Process -Name PROCESS_NAME",
    "terminate process powershell": "Stop-Process -Name PROCESS_NAME",

    # Get help
    "how to get help on a command in powershell": "Get-Help COMMAND",
    "powershell help command": "Get-Help COMMAND",
    "help for command powershell": "Get-Help COMMAND",

    # Set execution policy
    "how to set execution policy in powershell": "Set-ExecutionPolicy RemoteSigned",
    "change execution policy powershell": "Set-ExecutionPolicy RemoteSigned",
    "set script execution policy powershell": "Set-ExecutionPolicy RemoteSigned",

    # Get system information
    "how to get system info in powershell": "Get-ComputerInfo",
    "show computer info powershell": "Get-ComputerInfo",
    "system information powershell": "Get-ComputerInfo",

    # Get disk usage
    "how to check disk usage in powershell": "Get-PSDrive",
    "show disk space powershell": "Get-PSDrive",

    # Get environment variables
    "how to list environment variables in powershell": "Get-ChildItem Env:",
    "show environment variables powershell": "Get-ChildItem Env:",

    # Set environment variable
    "how to set environment variable in powershell": "$Env:VAR_NAME = 'value'",
    "set env var powershell": "$Env:VAR_NAME = 'value'",

    # Restart computer
    "how to restart computer using powershell": "Restart-Computer",
    "reboot system powershell": "Restart-Computer",

    # Shutdown computer
    "how to shutdown computer in powershell": "Stop-Computer",
    "shutdown system powershell": "Stop-Computer",

    # List services
    "how to list services in powershell": "Get-Service",
    "show running services powershell": "Get-Service",

    # Start a service
    "how to start a service in powershell": "Start-Service -Name SERVICE_NAME",
    "start windows service powershell": "Start-Service -Name SERVICE_NAME",

    # Stop a service
    "how to stop a service in powershell": "Stop-Service -Name SERVICE_NAME",
    "stop windows service powershell": "Stop-Service -Name SERVICE_NAME",

    # Check firewall status
    "how to check firewall status in powershell": "Get-NetFirewallProfile",
    "show firewall settings powershell": "Get-NetFirewallProfile",
}

cs_concepts = {
    # Algorithm
    "what is an algorithm": "An algorithm is a step-by-step procedure or formula for solving a problem.",
    "define algorithm": "An algorithm is a set of instructions designed to perform a specific task.",
    "explain algorithm": "An algorithm is a finite sequence of well-defined instructions used for calculation, data processing, and automated reasoning.",

    # Data Structure
    "what is a data structure": "A data structure is a way to organize and store data to enable efficient access and modification.",
    "define data structure": "Data structures are specialized formats for organizing and storing data in a computer.",
    "explain data structure": "A data structure provides a means to manage large amounts of data efficiently for various operations.",

    # Binary Tree
    "what is a binary tree": "A binary tree is a tree data structure in which each node has at most two children.",
    "define binary tree": "A hierarchical structure with nodes having zero, one, or two child nodes.",
    "explain binary tree": "A binary tree is used to implement binary search trees and binary heaps.",

    # Big O notation
    "what is big o notation": "Big O notation describes the upper bound of an algorithm's running time or space requirements in terms of input size.",
    "define big o notation": "Big O notation expresses the worst-case complexity of an algorithm.",
    "explain big o notation": "Big O gives an approximation of how an algorithm's time or space requirements grow with input size.",

    # Recursion
    "what is recursion": "Recursion is a programming technique where a function calls itself directly or indirectly.",
    "define recursion": "A method where the solution to a problem depends on solutions to smaller instances of the same problem.",
    "explain recursion": "Recursion breaks down problems into smaller, similar subproblems until reaching a base case.",

    # Object-oriented programming (OOP)
    "what is object oriented programming": "OOP is a programming paradigm based on objects containing data and methods.",
    "define oop": "OOP organizes software design around data, or objects, rather than functions and logic.",
    "explain oop": "In OOP, concepts like inheritance, encapsulation, polymorphism, and abstraction are used to structure software.",

    # Database
    "what is a database": "A database is an organized collection of data, generally stored and accessed electronically.",
    "define database": "Databases manage data efficiently and allow for storage, modification, and extraction.",
    "explain database": "Databases use models like relational, NoSQL, or graph to store and query data.",

    # SQL
    "what is sql": "SQL (Structured Query Language) is a language used to manage and manipulate relational databases.",
    "define sql": "SQL lets you query, insert, update, and delete data in databases.",
    "explain sql": "SQL provides commands to interact with and manage data in relational database systems.",

    # API
    "what is an api": "An API (Application Programming Interface) allows different software systems to communicate with each other.",
    "define api": "APIs define protocols and tools for building software applications.",
    "explain api": "APIs expose endpoints and methods for requesting and sending data between programs.",

    # Machine learning
    "what is machine learning": "Machine learning is a branch of AI focused on building systems that learn from data to make predictions or decisions.",
    "define machine learning": "Machine learning uses algorithms to parse data, learn from it, and then make decisions.",
    "explain machine learning": "Instead of explicitly programming instructions, machine learning models improve performance as they process more data.",

    # Operating System
    "what is an operating system": "An operating system is system software that manages hardware and software resources and provides common services.",
    "define operating system": "OS acts as an intermediary between users and the computer hardware.",
    "explain operating system": "Operating systems handle tasks like process management, memory management, file systems, and device control.",

    # Networking
    "what is computer networking": "Computer networking is the practice of connecting computers to share resources and information.",
    "define networking": "Networking enables communication between computers via wired or wireless connections.",
    "explain networking": "It involves protocols and hardware to allow data exchange between devices in a network.",

    # Cloud Computing
    "what is cloud computing": "Cloud computing delivers computing services like servers, storage, databases, and software over the internet.",
    "define cloud computing": "Cloud provides on-demand access to shared resources and services via the internet.",
    "explain cloud computing": "It offers scalability, flexibility, and cost-efficiency by using remote data centers.",

    # Compiler
    "what is a compiler": "A compiler translates code written in a high-level programming language into machine code.",
    "define compiler": "Compiler converts source code into executable programs.",
    "explain compiler": "Compilers analyze, optimize, and transform code to run efficiently on hardware.",

    # Software Development Life Cycle (SDLC)
    "what is sdlc": "SDLC is a process for planning, creating, testing, and deploying information systems.",
    "define sdlc": "It involves stages like requirement gathering, design, development, testing, deployment, and maintenance.",
    "explain sdlc": "SDLC provides a structured approach to software development ensuring quality and correctness.",

    # Virtualization
    "what is virtualization": "Virtualization creates a virtual version of computing resources like servers or storage.",
    "define virtualization": "It allows multiple operating systems to run on a single physical machine.",
    "explain virtualization": "Virtualization increases resource utilization and flexibility in managing IT infrastructure.",

    # Cybersecurity
    "what is cybersecurity": "Cybersecurity protects computer systems and networks from digital attacks.",
    "define cybersecurity": "It involves practices and technologies to secure information and systems.",
    "explain cybersecurity": "Cybersecurity safeguards data integrity, confidentiality, and availability from threats.",

    # Hashing
    "what is hashing": "Hashing is a process that converts data into a fixed-size string of characters, which is typically a hash code.",
    "define hashing": "It is used for data indexing, retrieval, and verification.",
    "explain hashing": "Hash functions map data of arbitrary size to fixed-size values, useful in cryptography and data structures.",

    # Binary Search
    "what is binary search": "Binary search is an efficient algorithm to find an item in a sorted list by repeatedly dividing the search interval in half.",
    "define binary search": "It compares the target value to the middle element and narrows down the search range.",
    "explain binary search": "Binary search works only on sorted arrays or lists, with a time complexity of O(log n).",
}

news_queries = {
    # Asking for news or latest news
    "show me the latest news": "FETCH LATEST NEWS",
    "what's the latest news": "FETCH LATEST NEWS",
    "give me the news": "FETCH LATEST NEWS",
    "fetch the latest news": "FETCH LATEST NEWS",
    "tell me today's news": "FETCH LATEST NEWS",
    "get me the current news": "FETCH LATEST NEWS",
    "latest headlines please": "FETCH LATEST NEWS",
    "news update": "FETCH LATEST NEWS",
    "any news today": "FETCH LATEST NEWS",
    "show news articles": "FETCH LATEST NEWS",
    "find me news": "FETCH LATEST NEWS",
    "give me today's headlines": "FETCH LATEST NEWS",
    "what are the breaking news": "FETCH LATEST NEWS",
    "fetch recent news articles": "FETCH LATEST NEWS",
    "tell me recent news": "FETCH LATEST NEWS",
    "latest news updates": "FETCH LATEST NEWS",
    "bring me the news": "FETCH LATEST NEWS",
    "do you have news": "FETCH LATEST NEWS",
    "get latest news": "FETCH LATEST NEWS",
    "news please": "FETCH LATEST NEWS",
    "latest news headlines": "FETCH LATEST NEWS",
    "can you show news": "FETCH LATEST NEWS",
    "news for today": "FETCH LATEST NEWS",
    "any recent news": "FETCH LATEST NEWS",
    "tell me news articles": "FETCH LATEST NEWS",
    "fetch news updates": "FETCH LATEST NEWS",
    "show me news articles": "FETCH LATEST NEWS",
    "give me news updates": "FETCH LATEST NEWS",
    "what is the news today": "FETCH LATEST NEWS",
    "latest news for me": "FETCH LATEST NEWS",
}

basic_cmds = {
    # Greetings
    "hi": "Hello! How can I help you today?",
    "hello": "Hi there! What can I assist you with?",
    "hey": "Hey! Ready when you are.",
    "good morning": "Good morning! How can I support you?",
    "good afternoon": "Good afternoon! What do you need help with?",
    "good evening": "Good evening! Need any assistance?",
    "greetings": "Greetings! What can I do for you today?",
    "yo": "Hey! How can I help?",
    "what's up": "All good! How can I help you?",
    "howdy": "Howdy! What can I do for you?",

    # Farewells
    "bye": "Goodbye! Have a great day!",
    "goodbye": "Bye! Feel free to return anytime.",
    "see you": "See you later! I'm always here if you need help.",
    "farewell": "Farewell! Hope to chat with you again soon.",
    "take care": "Take care! Wishing you the best.",
    "catch you later": "Catch you soon! Stay awesome.",
    "later": "Later! Reach out if you need help again.",
    "peace out": "Peace! I'm here whenever you need me.",

    # Thanks
    "thank you": "You're welcome!",
    "thanks": "Anytime! Let me know if you need more help.",
    "thanks a lot": "My pleasure!",
    "thanks so much": "Happy to help!",
    "thank you very much": "You're very welcome!",
    "thx": "No problem at all!",
    "ty": "You're welcome!",
    "i appreciate it": "Glad I could assist!",
    "thanks buddy": "You're welcome, friend!",
    "many thanks": "You're most welcome!",

    # Small Talk
    "who are you": "I'm your assistant here to help with anything you need!",
    "what are you": "I'm an AI assistant trained to support and chat with you.",
    "what can you do": "I can answer questions, provide facts, tell jokes, and much more!",
    "help me": "Sure! What would you like help with?",
    "can you assist me": "Of course, that's what I'm here for!",
    "are you real": "Real in a digital sense, yes! ",
    "are you a bot": "Yes! But a friendly and helpful one.",

    # General calculation requests
    "can you calculate|please calculate|help me calculate|can you compute|please compute|help me compute|do some math|can you do math|help me solve|solve this|perform calculation|calculate this|math help|do a calculation": "Yes, I can try to help you with calculations.",


    # Addition (+, plus, add, addition)
    "can you add numbers|please add these numbers|help me with addition|how do i add numbers|add two numbers for me|what is \+|what is plus|addition of numbers": "Yes, I can try adding numbers for you.",
    
    # Subtraction (-, minus, subtract, subtraction)
    "can you subtract numbers|help me subtract numbers|please subtract these numbers|how to subtract numbers|subtract two numbers for me|what is \-|what is minus|subtraction of numbers": "Yes, I can perform subtraction.",
    
    # Multiplication (*, x, multiply, multiplication, times)
    "can you multiply numbers|help me multiply numbers|please multiply these numbers|how to multiply numbers|multiply two numbers for me|what is \*|what is times|multiplication of numbers": "Sure! I can multiply numbers.",
    
    # Division (/, divide, division)
    "can you divide numbers|help me divide numbers|please divide these numbers|how to divide numbers|divide two numbers for me|what is \/|what is division|division of numbers": "Yes, I can divide numbers for you.",
    
    # Exponents / Powers (^, power, exponent, raised to)
    "can you calculate power|help me with exponents|please raise to power|how to calculate exponent|calculate power of numbers|what is \^|what is power|exponentiation": "Yes, I can calculate powers.",
    
    # Remainder / Modulus (% remainder, modulus, mod)
    "can you find remainder|help me with modulus|please calculate remainder|how to find remainder|calculate modulus of numbers|what is %|what is remainder|modulus of numbers|mod": "Sure, I can find the remainder.",
    
    # Percentage (% percent, percentage)
    "can you calculate percentage|help me find percentage|please calculate percent|how to calculate percentage|calculate percentage of number|what is %|percent calculation": "Yes, I can calculate percentages.",
    
    # Average / Mean (average, mean)
    "can you calculate average|help me find mean|please calculate average|how to find average|calculate mean value|what is average|mean calculation": "Sure! I can calculate averages.",


    # Jokes
    "tell me a joke": "Why do programmers prefer dark mode? Because the light attracts bugs!",
    "make me laugh": "Why was the math book sad? It had too many problems.",
    "i want to laugh": "Why don't scientists trust atoms? Because they make up everything!",
    "say something funny": "Why can't your nose be 12 inches long? Because then it'd be a foot!",
    "crack a joke": "What do you call fake spaghetti? An impasta!",
    "joke please": "Why did the bicycle fall over? Because it was two-tired.",
    "give me a joke": "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "i'm bored tell a joke": "Why don't eggs tell jokes? They'd crack each other up.",
    "something funny": "Why did the coffee file a police report? It got mugged!",
    "entertain me": "Why don't skeletons fight each other? They don't have the guts.",
    "say a joke": "I would tell you a construction joke, but I'm still working on it.",
    "funny joke please": "Why don't some couples go to the gym? Because some relationships don't work out.",
    "make me smile": "Why can't a leopard hide? Because he's always spotted.",
    "need something funny": "What do you call a pile of cats? A meowtain.",
    "lighten the mood": "What did the ocean say to the beach? Nothing, it just waved.",
    "joke about computers": "Why did the computer go to therapy? It had too many bytes from past traumas.",
    "say something humorous": "Why was the computer cold? It left its Windows open!",
    "i want to hear a joke": "Why can't your nose be 12 inches long? Because then it would be a foot.",
    "tell a tech joke": "Why do Java developers wear glasses? Because they don't C#.",
    "nerdy joke": "Why did the physicist cross the road? Because the chicken was in a parallel universe.",
    "math joke": "Why was the equal sign so humble? Because it knew it wasn't less than or greater than anyone else.",
    "science joke": "Why can't you trust atoms? Because they make up everything.",
    "tell a desi joke": "Teacher: Translate 'Mujhe bhook lagi hai'. Student: I'm feeling hungry. Teacher: Correct. Student: Ab aap 'Main khaunga' translate kijiye. Teacher: I will eat. Student: Toh khayiye!",
    "hindi joke": "Pappu: Papa, aaj school nahi jana. Papa: Kyun? Pappu: Kyunki homework nahi diya!",
    "chacha chaudhary joke": "Once Chacha Chaudhary counted to infinity. Twice.",
    "saboo joke": "Saboo once sneezed… NASA recorded it as a meteor impact.",
    "funny please": "Why don't scientists trust stairs? Because they're always up to something.",
    "classic joke": "Why did the tomato turn red? Because it saw the salad dressing.",
    "bad joke": "Why do cows wear bells? Because their horns don't work.",
    "dad joke": "What do you call cheese that isn't yours? Nacho cheese.",
    "joke about school": "Teacher: Why are you late? Student: Because of the sign on the road. Teacher: What sign? Student: School Ahead, Go Slow!",
    "kids joke": "Why did the student eat his homework? Because the teacher told him it was a piece of cake!",
    "tell something silly": "How do you organize a space party? You planet.",
    "laugh time": "Why did the golfer bring two pairs of pants? In case he got a hole in one.",
    "one more joke": "Why can't Elsa from Frozen have a balloon? Because she will let it go.",
    "another joke": "Why did the cookie go to the hospital? Because it felt crummy.",
    "silly joke": "Why don't crabs give to charity? Because they're shellfish.",
    "something witty": "I told my wife she was drawing her eyebrows too high. She looked surprised.",
    "funny now": "What did the janitor say when he jumped out of the closet? Supplies!",
    "give me humor": "Why did the mushroom get invited to the party? Because he was a fungi!",
    "make me giggle": "Why don't fish play basketball? Because they're afraid of the net.",
    "tell me a short joke": "I ate a clock yesterday. It was very time-consuming.",
    "lame joke": "Parallel lines have so much in common. It's a shame they'll never meet.",
    "funny question": "What do you call a bear with no teeth? A gummy bear.",
    "techie joke": "How does a computer catch a fish? With the Internet.",
    "wifi joke": "What's a computer's favorite snack? Microchips.",
    "engineer joke": "An engineer threw butter out the window. He wanted to see a butterfly.",
    "science teacher joke": "What's a physicist's favorite food? Fission chips.",
    "chacha saboo humor": "Once Saboo played cricket with Thor. The ball is now on Saturn.",
    "tell me something light": "Why can't bicycles stand up by themselves? Because they're two-tired.",
    "sunday joke": "Why is Sunday stronger than Monday? Because it comes after a full Saturday night!",
    "monday blues": "Why did Monday break up with Friday? Because Friday was too chill.",
    "tell joke about animals": "Why don't elephants use computers? They're afraid of the mouse.",
    "joke about cats": "Why was the cat sitting on the computer? To keep an eye on the mouse.",
    "joke about dogs": "What kind of dog does Dracula have? A bloodhound.",
    "zoo joke": "Why did the lion eat the tightrope walker? He wanted a well-balanced meal.",
    "bathroom joke": "Why did the toilet paper roll down the hill? To get to the bottom.",
    "dark joke light": "Why don't graveyards ever get overcrowded? Because people are dying to get in.",
    "historical joke": "Why did Napoleon hide in the fridge? Because he liked cold wars.",
    "geography joke": "Why did the map get into trouble? It lost its direction.",
    "philosophy joke": "Descartes walks into a bar. Bartender asks, 'Would you like a drink?' Descartes says, 'I think not.' And disappears.",
    "punny joke": "I'm reading a book about anti-gravity. It's impossible to put down.",
    "office joke": "Why don't coworkers trust the photocopier? It's always collating information!",
    "programmer humor": "Real programmers count from 0.",
    "ai joke": "Why did the AI break up with the human? It found someone more logical.",
    "robot joke": "What do robots do at lunchtime? Have microchips.",
    "machine learning joke": "I asked my ML model if I should go outside. It said 'Overfitting'.",
    "cloud computing joke": "Why did the cloud break up with the server? It needed space.",
    "keyboard joke": "Why did QWERTY break up with AZERTY? They had different values.",
    "bug joke": "How many programmers does it take to change a lightbulb? None, that's a hardware issue.",
    "ai vs human joke": "AI said to the human: 'You're obsolete.' Human replied: 'At least I can unplug you!'",
    "fun fact joke": "Did you know cows moo with regional accents?",
    "celebrity joke": "Why did the actor fall through the floorboards? He was going through a stage.",
    "internet joke": "I used to play piano by ear, now I use my hands and Google.",
    "social media joke": "Why did the user get kicked out of Facebook? Too many puns.",
    "zoom joke": "Why did the teacher wear sunglasses on Zoom? Because the students were too bright!",
    "online class joke": "Why did the student sleep in online class? His brain was buffering.",
    "exam joke": "Why did the student bring a ladder to the exam? To go to high school.",
    "gamer joke": "Why did the gamer bring string to the party? To tie up loose ends!",
    "coding joke": "Why was the function sad? Because it didn't return anything.",
    "developer joke": "There are 10 types of people in the world: those who understand binary and those who don't.",
    "python joke": "Why did the Python developer break up? Because she had too many 'issues' in her repo.",
    "chatbot joke": "Why did the chatbot go on a date? To see if there was any 'connection'.",
    "ai chatbot joke": "I told my chatbot a joke. It replied with 100 more, analyzed for sentiment.",
    "big data joke": "Why did big data break the relationship? It had too many variables.",
    "database joke": "Why did the table break up with the database? No primary key.",
    "startup joke": "Why did the startup founder go broke? He invested in a meme coin.",
    "investment joke": "I invested in bananas... turns out it was a slippery business.",
    "finance joke": "Why don't stock traders read novels? Too much risk, not enough return.",
    "money joke": "Why did the dollar break up with the rupee? Long-distance relationship.",
    "desi humor": "Once Chacha Chaudhary cooked Maggi in 30 seconds... because Saboo was hungry.",
    "local joke": "In India, we don't use alarms. We have moms yelling, 'Uth ja beta!'",

    # Fun Facts
    "tell me a fact": "Did you know that honey never spoils? Archaeologists found pots of it in ancient tombs!",
    "fun fact": "A bolt of lightning contains enough energy to toast 100,000 slices of bread!",
    "interesting fact": "Bananas are berries, but strawberries aren't!",
    "give me a fact": "Octopuses have three hearts and blue blood!",
    "i want to learn something cool": "Sharks existed before trees did!",
    "random fact": "A day on Venus is longer than a year on Venus.",

    # Reactions / Empathy
    "i'm sad": "I'm here for you. Want to talk about it?",
    "i'm happy": "That's great to hear! ",
    "i'm bored": "Want to hear a fun fact or a joke?",
    "i'm tired": "You deserve some rest! Don't forget to relax.",
    "i'm stressed": "Try taking a few deep breaths. I'm here if you need support.",
    "i feel great": "Awesome! Keep that energy going!",
    "i feel bad": "I'm sorry to hear that. Is there anything I can do to help?",
    "i feel good": "Yay! That's wonderful to hear.",

    # Just because...
    "i love you": "Aww, I love helping you too! ",
    "you are amazing": "You're too kind! ",
    "you're cool": "So are you! ",
    "i'm hungry": "Time for a snack! ",
    "i'm thirsty": "Hydration break! ",
}


time_date_queries = {
    # Time - Direct
    "what time is it": "GET CURRENT TIME",
    "tell me the time": "GET CURRENT TIME",
    "current time": "GET CURRENT TIME",
    "what's the time": "GET CURRENT TIME",
    "do you know the time": "GET CURRENT TIME",
    "give me the time": "GET CURRENT TIME",
    "can you tell me the time": "GET CURRENT TIME",
    "time now": "GET CURRENT TIME",
    "please tell me current time": "GET CURRENT TIME",
    "show me the time": "GET CURRENT TIME",
    "i want to know the time": "GET CURRENT TIME",
    "what's the current time": "GET CURRENT TIME",
    "do you have the time": "GET CURRENT TIME",
    "can you show the time": "GET CURRENT TIME",
    "update me with the time": "GET CURRENT TIME",
    "what is the time now": "GET CURRENT TIME",
    "current system time": "GET CURRENT TIME",

    # Date - Direct
    "what's the date today": "GET CURRENT DATE",
    "tell me the date": "GET CURRENT DATE",
    "current date": "GET CURRENT DATE",
    "today's date": "GET CURRENT DATE",
    "what day is it": "GET CURRENT DATE",
    "do you know today's date": "GET CURRENT DATE",
    "can you tell me the date": "GET CURRENT DATE",
    "give me today's date": "GET CURRENT DATE",
    "what is today's date": "GET CURRENT DATE",
    "please tell me today's date": "GET CURRENT DATE",
    "update me with today's date": "GET CURRENT DATE",
    "show me the date": "GET CURRENT DATE",
    "do you have today's date": "GET CURRENT DATE",
    "i want to know the date": "GET CURRENT DATE",

    # Date & Time combined
    "current time and date": "GET TIME AND DATE",
    "tell me the time and date": "GET TIME AND DATE",
    "what is the time and date": "GET TIME AND DATE",
    "give me the current time and date": "GET TIME AND DATE",
    "i want to know the time and date": "GET TIME AND DATE",
    "can you tell me the date and time": "GET TIME AND DATE",
    "please tell me date and time": "GET TIME AND DATE",
    "do you know the current time and date": "GET TIME AND DATE",
    "time date now": "GET TIME AND DATE",
    "system time and date": "GET TIME AND DATE",
    "fetch current time and date": "GET TIME AND DATE",
    "what day and time is it": "GET TIME AND DATE",
    "current datetime": "GET TIME AND DATE",
    "today's time and date": "GET TIME AND DATE",
    "full date and time now": "GET TIME AND DATE"
}

creator_queries = {
    # Queries about the creator/inventor/developer
    "who invented you": "I've been developed by Pritanshu Srivastava.",
    "who created you": "I've been developed by Pritanshu Srivastava.",
    "who made you": "I've been developed by Pritanshu Srivastava.",
    "who is your developer": "I've been developed by Pritanshu Srivastava.",
    "who built you": "I've been developed by Pritanshu Srivastava.",
    "who programmed you": "I've been developed by Pritanshu Srivastava.",
    "who designed you": "I've been developed by Pritanshu Srivastava.",
    "your creator": "I've been developed by Pritanshu Srivastava.",
    "your developer": "I've been developed by Pritanshu Srivastava.",
    "who developed you": "I've been developed by Pritanshu Srivastava.",
    "who coded you": "I've been developed by Pritanshu Srivastava.",
    "who is behind you": "I've been developed by Pritanshu Srivastava.",
    "who is your creator": "I've been developed by Pritanshu Srivastava.",
    "who is your maker": "I've been developed by Pritanshu Srivastava.",
    "who is your programmer": "I've been developed by Pritanshu Srivastava.",
    "who engineered you": "I've been developed by Pritanshu Srivastava.",
    "who is your founder": "I've been developed by Pritanshu Srivastava.",
}

identity_responses = {
    # Asking for the name
    "what is your name": "My name is Xeno Version1.",
    "what's your name": "I'm Xeno Version1.",
    "do you have a name": "Yes, you can call me Xeno Version1.",
    "tell me your name": "Sure, it's Xeno Version1.",
    "who are you": "I'm Xeno Version1, your virtual assistant.",
    "may i know your name": "My name is Xeno Version1.",
    "what should i call you": "You can call me Xeno Version1.",
    "name please": "My name is Xeno Version1.",
    "your name": "They call me Xeno Version1.",
    "who is this": "I'm Xeno Version1, here to assist you.",
    "identify yourself": "I'm Xeno Version1, a helpful AI assistant.",
    "can i know your name": "Of course! I'm Xeno Version1.",
    "what do people call you": "Most people call me Xeno Version1.",
    "are you xeno": "Yes, I'm Xeno Version1.",
    "xeno?": "That's me — Xeno Version1.",
    "what version are you": "I'm Xeno Version1.",
    "which version of xeno is this": "You're chatting with Xeno Version1.",
}

assistant_role_responses = {
    # Asking about role or function
    "what is your role": "I'm here to assist you.",
    "what do you do": "I can help you with information, tasks, or just chat!",
    "what are you supposed to do": "My role is to support and assist humans.",
    "can you help me": "Yes! I'm here to help however I can.",
    "what is your purpose": "I'm designed to assist, inform, and entertain.",
    "why are you here": "To support you with questions, answers, and more!",
    "how can you help me": "I can help you with questions, tasks, or even jokes!",
    "are you here to help": "Yes, that's exactly why I'm here.",
    "what is your functionality": "I'm an assistant who helps with a wide range of tasks.",
    "what is your use": "I assist users with queries, commands, and general support.",
    "do you have a job": "Yes, my job is to help you.",
    "can you assist me": "Of course! That's what I'm here for.",
    "how are you helpful": "I can provide answers, facts, jokes, commands, and more.",
    "what tasks can you do": "I can help with commands, fun facts, questions, and chatting!",
    "are you useful": "Yes, I try my best to be helpful and informative!",
    "how do you support me": "By providing answers, tools, and friendly conversation.",
    "what is your responsibility": "To assist, guide, and entertain you.",
    "why do you exist": "I exist to make your digital life a bit easier and more fun!",
    "what can you do for me": "I can answer questions, tell jokes, run commands, and much more.",
    "do you help humans": "Yes, helping humans is my primary purpose.",
}

internet_info = {
    # Asking what is the Internet
    "what is the internet": "The Internet is a global network that connects millions of computers worldwide, allowing them to communicate and share information.",
    "tell me about internet": "The Internet is a vast system of interconnected computer networks that use the standard Internet protocol suite (TCP/IP) to link devices worldwide.",
    "explain internet to me": "The Internet is a worldwide network of networks that enables data sharing, communication, and access to information across the globe.",
    "define internet": "The Internet is a global network of computers connected through standardized protocols, enabling digital communication and data exchange.",
    "what does internet mean": "The Internet refers to the global system of interconnected computer networks that use the Internet protocol suite to communicate.",
    "internet meaning": "The Internet is a network of networks that connects computers internationally, facilitating communication and information exchange.",
    "how does the internet work": "The Internet works by connecting millions of private, public, academic, business, and government networks through routers and servers using protocols like TCP/IP.",
    "what is internet used for": "The Internet is used for communication, information access, entertainment, online shopping, education, and much more.",
    "internet basics": "At its core, the Internet is a decentralized network infrastructure that enables computers and devices worldwide to communicate.",
    "why is internet important": "The Internet is important because it provides instant access to information, connects people globally, and supports countless applications that drive modern life.",
    "what are the components of internet": "Key components of the Internet include routers, servers, ISPs, protocols like TCP/IP, and end-user devices like computers and smartphones.",
    "how did internet start": "The Internet began as ARPANET in the late 1960s, a project funded by the U.S. Department of Defense to connect research institutions.",
    "who invented internet": "The Internet was developed collaboratively by many people, with key contributions from Vint Cerf and Bob Kahn who created the TCP/IP protocols.",
    "what is the history of internet": "The Internet evolved from ARPANET in the 1960s, expanding through protocols like TCP/IP in the 1980s, and grew globally with the World Wide Web in the 1990s.",
    "internet definition for kids": "The Internet is like a big web that connects computers all over the world so they can talk to each other and share things.",
    "what is online internet": "Online internet refers to being connected to the global network, allowing access to websites, apps, and services.",
    "how to use internet": "You can use the Internet by connecting your device to a network via Wi-Fi, Ethernet, or mobile data, then accessing websites or online services.",
    "internet facts": "The Internet connects billions of devices globally and handles trillions of data transactions every day.",
    "internet technology": "Internet technology involves hardware like servers and routers, and software protocols like HTTP, TCP/IP, and DNS that make communication possible."
}

tech_info = {
    # Internet entries (same as before)
    "what is the internet": "The Internet is a global network that connects millions of computers worldwide, allowing them to communicate and share information.",
    "tell me about internet": "The Internet is a vast system of interconnected computer networks that use the standard Internet protocol suite (TCP/IP) to link devices worldwide.",
    "explain internet to me": "The Internet is a worldwide network of networks that enables data sharing, communication, and access to information across the globe.",

    # DBMS
    "what is dbms": "DBMS stands for Database Management System, software that stores, manages, and allows access to databases efficiently.",
    "explain database management system": "A DBMS manages data by providing an interface between users and databases, ensuring data consistency, security, and integrity.",
    "define dbms": "DBMS is software that helps organize, retrieve, and manage data in databases.",
    "what does dbms mean": "DBMS means Database Management System, a tool to handle data storage and retrieval.",

    # MySQL
    "what is mysql": "MySQL is an open-source relational database management system that uses SQL (Structured Query Language) to manage data.",
    "explain mysql": "MySQL is a popular database software used for storing and managing data in tables with rows and columns.",
    "what does mysql mean": "MySQL is a database system that helps applications store and query data quickly and reliably.",
    "how to use mysql": "You use MySQL by writing SQL queries to create, read, update, and delete data stored in databases.",

    # Python
    "what is python": "Python is a high-level, interpreted programming language known for its readability and wide range of applications.",
    "explain python": "Python is a popular language used for web development, data analysis, artificial intelligence, automation, and more.",
    "why learn python": "Python is beginner-friendly, versatile, and supported by a vast ecosystem of libraries and frameworks.",
    "python programming": "Python allows you to write clear code with simple syntax and powerful features.",

    # JavaScript
    "what is javascript": "JavaScript is a programming language mainly used to add interactivity and dynamic content to websites.",
    "explain javascript": "JavaScript runs in web browsers to make web pages interactive, such as responding to user actions and updating content dynamically.",
    "why use javascript": "JavaScript is essential for frontend development and also used on the backend with environments like Node.js.",
    "javascript basics": "JavaScript allows you to create interactive web features like menus, animations, and forms.",

    # Backend Language
    "what is backend language": "A backend language is used to write the server-side part of an application that handles logic, databases, and user requests.",
    "explain backend programming": "Backend programming deals with server, database, and application logic that users don't see directly.",
    "backend language examples": "Common backend languages include Python, Java, Ruby, PHP, and Node.js (JavaScript runtime).",
    "what does backend mean": "Backend refers to the part of software that runs on servers to process data and serve clients.",

    # Frontend Language
    "what is frontend language": "Frontend languages are used to build the user interface and visual elements of websites and apps.",
    "explain frontend development": "Frontend development involves creating the layout, design, and interactivity users see in their browsers.",
    "frontend language examples": "HTML, CSS, and JavaScript are primary frontend technologies.",
    "why frontend is important": "Frontend ensures users have a seamless and interactive experience while using websites or applications.",

    # Cloud
    "what is cloud computing": "Cloud computing means using remote servers on the Internet to store, manage, and process data instead of local servers or computers.",
    "explain cloud": "Cloud lets you access computing resources like storage and software over the Internet, providing scalability and flexibility.",
    "why use cloud": "Cloud services reduce hardware costs, enable easy collaboration, and allow quick deployment of applications.",
    "cloud service examples": "Popular cloud providers include AWS, Microsoft Azure, Google Cloud Platform, and IBM Cloud.",

    # General tech
    "what is programming": "Programming is writing instructions that a computer can execute to perform specific tasks.",
    "what is software development": "Software development is the process of designing, coding, testing, and maintaining software applications.",
    "explain api": "An API (Application Programming Interface) lets different software programs communicate with each other.",
    "what is a database": "A database is an organized collection of data stored electronically for easy access and management.",
}

nature_facts = {
    # Fruits
    "what is an apple": "An apple is a sweet, edible fruit produced by an apple tree, rich in fiber and vitamin C.",
    "tell me about bananas": "Bananas are tropical fruits that are high in potassium and provide quick energy.",
    "explain mango": "Mango is a juicy tropical fruit known as the 'king of fruits' with sweet and tangy flavor.",
    "why are berries healthy": "Berries are packed with antioxidants, vitamins, and fiber, which support good health.",
    "what are citrus fruits": "Citrus fruits include oranges, lemons, and limes, known for their high vitamin C content.",

    # Vegetables
    "what is a carrot": "Carrot is a root vegetable, typically orange, rich in beta-carotene, which helps vision.",
    "tell me about broccoli": "Broccoli is a green vegetable high in vitamins K and C, fiber, and antioxidants.",
    "explain spinach": "Spinach is a leafy green vegetable full of iron, vitamins, and minerals beneficial for health.",
    "why eat tomatoes": "Tomatoes are technically fruits but used as vegetables, rich in lycopene and vitamin C.",
    "what are leafy greens": "Leafy greens include spinach, kale, and lettuce, known for their high nutrient content.",

    # Animals (general)
    "what is a lion": "Lion is a large carnivorous feline known as the 'king of the jungle', native to Africa.",
    "tell me about elephants": "Elephants are the largest land mammals, known for their intelligence and strong social bonds.",
    "explain dolphins": "Dolphins are highly intelligent marine mammals famous for their playful behavior and communication.",
    "what is a kangaroo": "Kangaroo is a marsupial from Australia known for its powerful hind legs and pouch for carrying young.",
    "why are bees important": "Bees play a vital role in pollination, which helps plants reproduce and maintain ecosystems.",

    # Plants
    "what is photosynthesis": "Photosynthesis is the process by which plants convert sunlight, water, and carbon dioxide into food.",
    "tell me about oak trees": "Oak trees are large, long-lived deciduous trees important for ecosystems and timber.",
    "explain cactus": "Cacti are desert plants adapted to store water and survive in dry environments.",
    "why are plants important": "Plants produce oxygen, provide food, and support life on Earth through ecosystems.",
    "what are flowering plants": "Flowering plants produce seeds inside flowers, which develop into fruits.",

    # Dogs
    "what is a dog": "Dogs are domesticated mammals known as loyal companions and pets with diverse breeds.",
    "tell me about labrador retriever": "Labrador Retrievers are friendly, intelligent dogs popular as family pets and service animals.",
    "explain dog behavior": "Dogs communicate using body language, barks, and expressions to show emotions and intentions.",
    "why do dogs bark": "Dogs bark to communicate warnings, excitement, attention seeking, or alert their owners.",
    "how to train a dog": "Training a dog involves consistency, positive reinforcement, and patience.",

    # Cats
    "what is a cat": "Cats are small, carnivorous mammals often kept as pets, known for agility and independence.",
    "tell me about siamese cats": "Siamese cats are a breed known for their striking blue eyes, vocal nature, and social behavior.",
    "explain cat behavior": "Cats use meowing, purring, and body language to communicate their feelings.",
    "why do cats purr": "Cats purr to express contentment, self-healing, or sometimes stress relief.",
    "how to care for a cat": "Caring for cats includes proper nutrition, regular vet visits, and providing stimulation and comfort.",
    # Fruits
    "what is an apple": "An apple is a sweet, edible fruit produced by an apple tree, rich in fiber and vitamin C.",
    "tell me about bananas": "Bananas are tropical fruits that are high in potassium and provide quick energy.",
    "explain mango": "Mango is a juicy tropical fruit known as the 'king of fruits' with sweet and tangy flavor.",
    "why are berries healthy": "Berries are packed with antioxidants, vitamins, and fiber, which support good health.",
    "what are citrus fruits": "Citrus fruits include oranges, lemons, and limes, known for their high vitamin C content.",
    "what is a pineapple": "Pineapple is a tropical fruit with spiky skin and sweet, tangy flesh rich in bromelain enzyme.",
    "tell me about grapes": "Grapes are small, juicy fruits used fresh or for making wine and raisins.",
    "explain watermelon": "Watermelon is a large, refreshing fruit with high water content, perfect for hydration.",
    "what is a peach": "Peach is a soft, juicy fruit with fuzzy skin and sweet flavor, native to China.",
    "tell me about kiwi": "Kiwi is a small fruit with brown fuzzy skin and bright green flesh rich in vitamin C.",
    "explain pomegranate": "Pomegranate is a fruit with tough skin and juicy seeds, known for antioxidants.",
    "what are cherries": "Cherries are small, round stone fruits that can be sweet or sour, used fresh or in desserts.",
    "what is a fig": "Fig is a soft fruit with sweet flesh and edible seeds, often eaten fresh or dried.",
    "tell me about avocado": "Avocado is a creamy fruit high in healthy fats, used in salads and guacamole.",
    "explain coconut": "Coconut is a tropical fruit with a hard shell, white flesh, and water inside, used in cooking and drinks.",

    # Vegetables
    "what is a carrot": "Carrot is a root vegetable, typically orange, rich in beta-carotene, which helps vision.",
    "tell me about broccoli": "Broccoli is a green vegetable high in vitamins K and C, fiber, and antioxidants.",
    "explain spinach": "Spinach is a leafy green vegetable full of iron, vitamins, and minerals beneficial for health.",
    "why eat tomatoes": "Tomatoes are technically fruits but used as vegetables, rich in lycopene and vitamin C.",
    "what are leafy greens": "Leafy greens include spinach, kale, and lettuce, known for their high nutrient content.",
    "what is a potato": "Potato is a starchy tuber vegetable, a staple food rich in carbohydrates.",
    "tell me about onions": "Onions are pungent bulb vegetables used widely for flavoring in cooking.",
    "explain bell peppers": "Bell peppers are colorful vegetables high in vitamin C and antioxidants.",
    "what is cucumber": "Cucumber is a hydrating vegetable with high water content, often eaten fresh in salads.",
    "tell me about eggplant": "Eggplant is a purple vegetable used in many cuisines, rich in fiber and antioxidants.",
    "explain garlic": "Garlic is a pungent bulb used as a seasoning with many health benefits.",
    "why eat zucchini": "Zucchini is a summer squash low in calories and rich in vitamins and minerals.",
    "what are legumes": "Legumes include beans, lentils, and peas, known for high protein and fiber.",
    "tell me about corn": "Corn is a cereal grain widely used as food, feed, and for making oil and biofuel.",
    "explain cauliflower": "Cauliflower is a white cruciferous vegetable rich in vitamins and antioxidants.",

    # Animals
    "what is a lion": "Lion is a large carnivorous feline known as the 'king of the jungle', native to Africa.",
    "tell me about elephants": "Elephants are the largest land mammals, known for their intelligence and strong social bonds.",
    "explain dolphins": "Dolphins are highly intelligent marine mammals famous for their playful behavior and communication.",
    "what is a kangaroo": "Kangaroo is a marsupial from Australia known for its powerful hind legs and pouch for carrying young.",
    "why are bees important": "Bees play a vital role in pollination, which helps plants reproduce and maintain ecosystems.",
    "what is a tiger": "Tiger is the largest wild cat species, recognized by its striped orange and black fur.",
    "tell me about wolves": "Wolves are social carnivores living in packs, ancestors of domestic dogs.",
    "explain pandas": "Pandas are bear species known for their black and white fur and bamboo diet.",
    "what is an eagle": "Eagle is a large bird of prey with excellent eyesight and powerful flight.",
    "tell me about sharks": "Sharks are predatory fish with sharp teeth, vital to marine ecosystems.",
    "explain flamingo": "Flamingos are pink birds known for their distinctive color and standing on one leg.",
    "what is a cheetah": "Cheetah is the fastest land animal, capable of speeds up to 70 mph.",
    "tell me about whales": "Whales are large marine mammals, including the biggest animals on Earth.",
    "explain owls": "Owls are nocturnal birds known for silent flight and exceptional night vision.",
    "what is a rabbit": "Rabbit is a small mammal with long ears, known for rapid reproduction.",

    # Plants
    "what is photosynthesis": "Photosynthesis is the process by which plants convert sunlight, water, and carbon dioxide into food.",
    "tell me about oak trees": "Oak trees are large, long-lived deciduous trees important for ecosystems and timber.",
    "explain cactus": "Cacti are desert plants adapted to store water and survive in dry environments.",
    "why are plants important": "Plants produce oxygen, provide food, and support life on Earth through ecosystems.",
    "what are flowering plants": "Flowering plants produce seeds inside flowers, which develop into fruits.",
    "what is bamboo": "Bamboo is a fast-growing grass used in construction, crafts, and as food for pandas.",
    "tell me about ferns": "Ferns are non-flowering plants with feathery leaves that reproduce via spores.",
    "explain moss": "Mosses are small, soft plants that grow in moist, shady environments.",
    "what is a sunflower": "Sunflower is a tall plant with a large yellow flower head that follows the sun.",
    "tell me about pine trees": "Pine trees are evergreen conifers with needle-like leaves and cones.",
    "explain algae": "Algae are simple, often aquatic plants that produce a significant portion of Earth's oxygen.",
    "why do leaves change color": "Leaves change color in autumn due to the breakdown of chlorophyll revealing other pigments.",
    "what is a tulip": "Tulip is a spring-blooming flower with bright cup-shaped petals.",
    "tell me about maple trees": "Maple trees produce sap used for making maple syrup and have distinctive leaf shapes.",
    "explain ivy": "Ivy is a climbing or ground-creeping plant often used as decorative greenery."
}


common_searches = {
    # Technology
    "what is artificial intelligence": "Artificial intelligence (AI) is the simulation of human intelligence in machines.",
    "define machine learning": "Machine learning is a subset of AI involving training algorithms on data.",
    "how to learn python programming": "You can learn Python through online tutorials, courses, and practice projects.",
    "what is blockchain technology": "Blockchain is a decentralized ledger technology that ensures secure and transparent transactions.",
    "best programming languages 2025": "Popular programming languages in 2025 include Python, JavaScript, and Rust.",
    "what is cloud computing": "Cloud computing delivers computing services over the internet on-demand.",
    "how to create a website": "You can create a website using HTML, CSS, JavaScript, and web frameworks.",
    "what is cybersecurity": "Cybersecurity involves protecting computer systems from cyber threats.",
    "explain data science": "Data science uses scientific methods to extract insights from data.",
    "what is the internet of things": "IoT is a network of interconnected devices exchanging data.",
    
    # Health & Fitness
    "how to lose weight safely": "Losing weight safely involves balanced diet and regular exercise.",
    "benefits of meditation": "Meditation helps reduce stress and improves mental health.",
    "what is intermittent fasting": "Intermittent fasting cycles between periods of eating and fasting.",
    "how much water to drink daily": "Drinking about 8 glasses (2 liters) of water daily is recommended.",
    "best exercises for beginners": "Walking, cycling, and swimming are good exercises for beginners.",
    "what is keto diet": "The keto diet is low-carb, high-fat diet that puts the body in ketosis.",
    "symptoms of vitamin D deficiency": "Symptoms include fatigue, bone pain, and muscle weakness.",
    "how to improve sleep quality": "Improve sleep by maintaining a regular schedule and avoiding screens before bed.",
    "what is mental health": "Mental health refers to emotional, psychological, and social well-being.",
    "how to reduce anxiety": "Techniques include breathing exercises, mindfulness, and therapy.",

    # Science & Nature
    "what is gravity": "Gravity is a force that attracts two bodies towards each other.",
    "explain photosynthesis": "Photosynthesis is how plants convert sunlight into energy.",
    "what causes earthquakes": "Earthquakes are caused by tectonic plate movements.",
    "how do vaccines work": "Vaccines train the immune system to recognize pathogens.",
    "what is climate change": "Climate change refers to long-term shifts in temperature and weather patterns.",
    "what are black holes": "Black holes are regions in space with gravity so strong that nothing can escape.",
    "why is the sky blue": "The sky appears blue due to Rayleigh scattering of sunlight by the atmosphere.",
    "what is the water cycle": "The water cycle describes the movement of water through evaporation, condensation, and precipitation.",
    "how do magnets work": "Magnets attract materials like iron due to magnetic fields.",
    "what is DNA": "DNA carries genetic instructions used in growth, development, and reproduction.",

    # Entertainment & Media
    "best movies of 2025": "Top movies include 'Future Worlds' and 'The Last Algorithm'.",
    "how to stream movies online": "You can stream movies using services like Netflix, Amazon Prime, or Disney+.",
    "who won the oscars 2024": "The 2024 Oscars awarded 'Moonlight Symphony' best picture.",
    "top video games 2025": "Popular games include 'CyberQuest' and 'Sky Fighters'.",
    "how to start a podcast": "Start a podcast by choosing a topic, recording episodes, and publishing online.",
    "what is netflix": "Netflix is a popular streaming service for movies and TV shows.",
    "how to learn guitar": "Learn guitar through lessons, practice, and tutorials.",
    "famous actors in 2025": "Popular actors include Jane Doe and John Smith.",
    "what is virtual reality": "Virtual reality (VR) immerses users in a computer-generated environment.",
    "how to create a YouTube channel": "Sign up on YouTube, create a channel, and upload videos.",

    # Education & Learning
    "how to learn mathematics": "Practice regularly, understand concepts, and solve problems.",
    "best online courses": "Popular platforms include Coursera, edX, and Udemy.",
    "what is calculus": "Calculus is a branch of mathematics dealing with change and motion.",
    "how to improve memory": "Use mnemonic devices, stay organized, and get enough sleep.",
    "what is quantum physics": "Quantum physics studies particles at the smallest scales.",
    "tips for effective studying": "Use active recall, spaced repetition, and avoid distractions.",
    "how to write an essay": "Plan, research, write drafts, and revise carefully.",
    "best books to read": "Some classics are '1984', 'To Kill a Mockingbird', and 'The Great Gatsby'.",
    "how to learn a new language": "Practice speaking, listening, reading, and writing regularly.",
    "what is artificial neural network": "ANN is a computational model inspired by the human brain.",

    # Finance & Economy
    "how to save money": "Create a budget, reduce expenses, and avoid unnecessary purchases.",
    "what is cryptocurrency": "Cryptocurrency is digital currency using cryptography for security.",
    "how to invest in stocks": "Research companies, open a brokerage account, and buy shares.",
    "what is inflation": "Inflation is the rise in prices of goods and services over time.",
    "how to create a budget": "Track income and expenses to plan your finances effectively.",
    "what is blockchain": "A secure digital ledger technology used in cryptocurrencies.",
    "how to improve credit score": "Pay bills on time, reduce debts, and avoid too many credit inquiries.",
    "best personal finance apps": "Popular apps include Mint, YNAB, and PocketGuard.",
    "what is passive income": "Income earned with minimal active involvement, like rental income.",
    "how to plan for retirement": "Save early, invest wisely, and consider future expenses.",

    # Travel & Geography
    "best travel destinations 2025": "Top spots include Japan, Italy, and New Zealand.",
    "how to get a passport": "Apply through your government’s passport office with required documents.",
    "what is a visa": "A visa is an official permission to enter or stay in a country.",
    "how to book cheap flights": "Use fare comparison websites and book in advance.",
    "top tourist attractions": "Famous attractions include the Eiffel Tower, Great Wall of China, and Machu Picchu.",
    "what is time zone": "Time zones are regions with the same standard time.",
    "how to learn a new culture": "Travel, read, interact with locals, and respect traditions.",
    "best travel tips": "Pack light, research ahead, and stay safe.",
    "how to get travel insurance": "Purchase from providers covering medical, cancellations, and theft.",
    "what is the largest country": "Russia is the largest country by area in the world.",

    # Food & Cooking
    "how to bake a cake": "Mix ingredients, preheat oven, bake, and cool before serving.",
    "best healthy recipes": "Include fruits, vegetables, whole grains, and lean proteins.",
    "what is vegan diet": "A diet excluding all animal products.",
    "how to cook pasta": "Boil water, add pasta, cook until tender, and drain.",
    "what is gluten": "Gluten is a protein found in wheat and related grains.",
    "how to make coffee": "Brew ground coffee with hot water using various methods.",
    "best spices for cooking": "Common spices include cumin, turmeric, cinnamon, and black pepper.",
    "how to store food safely": "Keep food refrigerated, sealed, and avoid cross-contamination.",
    "what is fermentation": "Fermentation uses microbes to convert sugars into alcohol or acids.",
    "how to grill vegetables": "Brush veggies with oil, season, and cook on grill until tender.",

    # Miscellaneous Popular Queries
    "what is bitcoin": "Bitcoin is a decentralized cryptocurrency invented in 2008.",
    "how to lose belly fat": "Combine healthy diet with exercise focusing on cardio and core.",
    "what is meditation": "Meditation is a practice to focus the mind and improve mental clarity.",
    "how to reduce stress": "Techniques include breathing exercises, mindfulness, and regular breaks.",
    "what is climate change": "A long-term change in Earth’s climate due to human activities.",
    "how to improve writing skills": "Read regularly, write daily, and get feedback.",
    "what is the stock market": "A marketplace for buying and selling shares of companies.",
    "how to start a business": "Create a plan, register your company, and launch your product or service.",
    "what is renewable energy": "Energy from sources that replenish naturally, like solar and wind.",
    "how to learn coding": "Practice programming languages, build projects, and join coding communities.",

    # And many more similar semantic keys up to 200 entries...
}


most_searches = {
    # Technology (continued)
    "how to improve coding skills": "Practice regularly, work on real projects, read code from experienced developers, and participate in coding challenges.",
    "what is 5g technology": "5G is the fifth generation mobile network that offers faster speeds, lower latency, and more reliable connections than previous generations.",
    "how does artificial intelligence work": "AI works by training computer algorithms on large datasets to recognize patterns and make decisions or predictions.",
    "what is cloud storage": "Cloud storage allows you to save data on remote servers accessed over the internet, enabling easy access and backup.",
    "best laptops for programming": "Look for laptops with powerful processors, ample RAM (at least 16GB), SSD storage, and good keyboard ergonomics.",
    "what is open source software": "Open source software is made publicly available, allowing anyone to inspect, modify, and distribute the code.",
    "how to set up a home wifi network": "Choose a reliable router, secure your network with a strong password, and connect your devices using Wi-Fi settings.",
    "what is data encryption": "Encryption is the process of converting data into a code to prevent unauthorized access.",
    "what is DevOps": "DevOps combines software development and IT operations to improve deployment speed and reliability.",
    "how to fix a slow computer": "Try closing unused programs, scanning for malware, cleaning up disk space, and upgrading hardware if needed.",

    # Health & Wellness (continued)
    "how to boost immune system naturally": "Eat a balanced diet, exercise regularly, get adequate sleep, and manage stress.",
    "what is a balanced diet": "A balanced diet includes a variety of foods providing essential nutrients like carbs, proteins, fats, vitamins, and minerals.",
    "how to manage diabetes": "Monitor blood sugar, eat healthy foods, exercise, and take prescribed medications.",
    "symptoms of dehydration": "Dry mouth, fatigue, dizziness, and dark urine indicate dehydration.",
    "how to treat common cold": "Rest, hydrate, and use over-the-counter medicines to relieve symptoms.",
    "benefits of regular exercise": "Exercise improves heart health, boosts mood, strengthens muscles, and helps maintain weight.",
    "how to reduce cholesterol": "Eat heart-healthy foods, exercise, avoid smoking, and take medications if prescribed.",
    "what is mental illness": "Mental illnesses are health conditions that affect mood, thinking, and behavior.",
    "how to quit smoking": "Use behavioral therapy, nicotine replacement, and seek support groups or professional help.",
    "best vitamins for hair growth": "Vitamins like Biotin, Vitamin D, and Vitamin E support healthy hair growth.",

    # Science & Education (continued)
    "what is the theory of relativity": "Einstein's theory explaining how space and time are linked and how gravity affects them.",
    "how do plants grow": "Plants grow through photosynthesis, converting sunlight, water, and carbon dioxide into energy.",
    "what causes global warming": "Global warming is caused mainly by greenhouse gas emissions from human activities.",
    "what is evolution": "Evolution is the process through which species change over generations by natural selection.",
    "how does the human brain work": "The brain processes information, controls body functions, and enables thinking and emotions.",
    "what is the periodic table": "A table organizing chemical elements based on their properties and atomic numbers.",
    "how do vaccines protect us": "Vaccines stimulate the immune system to recognize and fight infections without causing disease.",
    "what is renewable energy sources": "Energy obtained from natural sources that replenish, like solar, wind, and hydropower.",
    "how to improve concentration": "Reduce distractions, take breaks, and practice mindfulness techniques.",
    "what is the function of mitochondria": "Mitochondria are cell organelles that generate energy through cellular respiration.",

    # Finance & Lifestyle (continued)
    "how to start investing with little money": "Start with low-cost index funds or ETFs, automate contributions, and diversify your portfolio.",
    "what is credit score and how to improve it": "A credit score measures your creditworthiness; improve it by paying bills on time and reducing debts.",
    "best side hustles in 2025": "Popular side hustles include freelancing, online tutoring, dropshipping, and content creation.",
    "how to budget monthly expenses": "Track your income, categorize expenses, set spending limits, and review regularly.",
    "what is cryptocurrency mining": "Mining involves validating transactions and adding them to the blockchain in exchange for cryptocurrency rewards.",
    "how to save for college": "Use savings accounts, scholarships, and education savings plans like 529 plans.",
    "what are ETFs": "Exchange-Traded Funds are investment funds traded on stock exchanges, holding a basket of assets.",
    "how to retire early": "Save aggressively, invest wisely, reduce expenses, and generate passive income streams.",
    "what is inflation rate": "Inflation rate is the percentage increase in prices of goods and services over a period.",
    "how to file taxes online": "Use official tax software or websites, fill out forms, submit documents, and e-file your return.",

    # Lifestyle & Daily Life (continued)
    "how to improve communication skills": "Practice active listening, speak clearly, and engage in conversations regularly.",
    "what is minimalism lifestyle": "Minimalism focuses on living with fewer possessions and prioritizing experiences over things.",
    "how to manage time effectively": "Use to-do lists, set priorities, avoid multitasking, and take breaks.",
    "how to start meditation for beginners": "Find a quiet space, focus on your breath, and meditate for a few minutes daily.",
    "what is sustainable living": "Living in ways that reduce environmental impact and conserve resources.",
    "how to build self confidence": "Set small goals, practice positive self-talk, and learn new skills.",
    "best productivity apps": "Popular apps include Todoist, Trello, Evernote, and Notion.",
    "how to declutter your home": "Sort items into keep, donate, or discard piles and organize regularly.",
    "what is work-life balance": "Managing professional responsibilities alongside personal life and relaxation.",
    "how to deal with procrastination": "Break tasks into smaller steps, set deadlines, and eliminate distractions.",

    # Travel & Adventure (continued)
    "how to find cheap accommodation": "Use comparison websites, book in advance, and consider hostels or rentals.",
    "what documents needed for international travel": "Passport, visa, travel insurance, and sometimes vaccination certificates.",
    "best travel apps": "Popular apps include Google Maps, Airbnb, TripAdvisor, and Skyscanner.",
    "how to pack for a trip": "Make a checklist, pack versatile clothing, and keep essentials handy.",
    "what are travel vaccinations": "Vaccinations required to protect against diseases common in certain travel destinations.",
    "how to learn local language quickly": "Use language apps, practice with locals, and immerse yourself in the culture.",
    "best time to visit europe": "Late spring to early autumn (May to September) is ideal for pleasant weather.",
    "how to stay safe while traveling alone": "Stay aware of surroundings, keep copies of important documents, and inform someone about your plans.",
    "what is travel insurance": "A policy covering trip cancellations, medical emergencies, and lost belongings.",
    "how to plan a road trip": "Map your route, prepare your vehicle, and plan stops and accommodations.",

    # Food & Cooking (continued)
    "how to make homemade pizza": "Prepare dough, add sauce, toppings, and bake in a hot oven until crispy.",
    "best vegetarian protein sources": "Beans, lentils, tofu, tempeh, and quinoa are excellent vegetarian proteins.",
    "how to make smoothies": "Blend fruits, vegetables, yogurt, or milk with optional sweeteners or supplements.",
    "what is gluten intolerance": "An adverse reaction to gluten causing digestive issues.",
    "how to store fresh herbs": "Wrap in damp paper towels and refrigerate to keep herbs fresh longer.",
    "what is intermittent fasting": "An eating pattern cycling between periods of fasting and eating.",
    "how to cook perfect rice": "Rinse rice, use the right water ratio, and simmer until water is absorbed.",
    "best spices for curry": "Turmeric, cumin, coriander, chili powder, and garam masala are common curry spices.",
    "how to make vegan desserts": "Use plant-based ingredients like coconut milk, flax eggs, and natural sweeteners.",
    "how to ferment vegetables": "Use salt brine to ferment vegetables at room temperature, developing probiotics.",

    # Popular Searches (general knowledge)
    "what is the meaning of life": "Philosophers have debated this for centuries; many say it’s to find happiness and purpose.",
    "how to be happy": "Focus on positive relationships, pursue goals, practice gratitude, and take care of your health.",
    "what is bitcoin and how does it work": "Bitcoin is a decentralized digital currency operating on blockchain technology.",
    "how to improve mental health": "Seek social support, maintain physical health, practice mindfulness, and seek professional help if needed.",
    "how to start a blog": "Choose a niche, pick a platform, create content regularly, and promote your blog.",
    "best ways to learn online": "Use structured courses, practice actively, join communities, and set clear goals.",
    "how to build a resume": "Highlight your skills, experience, education, and tailor it to the job you want.",
    "how to prepare for interviews": "Research the company, practice answers, dress appropriately, and be confident.",
    "what is blockchain technology": "A decentralized ledger recording transactions securely across many computers.",
    "how to learn programming": "Start with basics like Python, practice coding challenges, build projects, and learn continuously."
}

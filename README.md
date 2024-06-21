# File Transfer using TCP Socket in Python3
A simple client-server program, where client send a file to server. 

Table of Contents
The Problem Statement	3
Details About the Hardware and Software Used in The Project	4
Results and Discussions	4
Server-Side Code	4
Server Side Output	7
Client Side Code	9
Client-Side Output (CMD)	11
References	14
Appendix	15
Server-Side Code	15
Client-Side Code	17
Server-Side Terminal Output	19
Client-Side Terminal Output	20


Socket Programming with Python: File Upload Project
Exams are vital for the academic development of students since they enable them to showcase their competence and understanding of the course content and solidify their knowledge in the required field (Gneezy et al., 2019). Multiple issues impede students in their learning journey, inhibiting their navigation through the academic system, such as poor time management. It is their role and duty to ensure they are well organized and finish their assignments and other scheduled tasks on time. This study has highlighted the various problems students face and will solve them by developing an application interface for uploading files to organize their work. A file management system project will assist students in alleviating their hustle in accessing study materials, increasing learning outcomes. 
The Problem Statement
At the classroom level, especially during the examination periods, students can struggle to organize and access their study resources (Laksana, 2020). Based on learner’s experiences, conventional organizational techniques, such as handwritten notes and tangible papers, are laborious and prone to loss or misplacing. Since learning is dynamic, students must learn to be flexible in incorporating new information into their systems and editing previously taught material. Students also face challenges in easily accessing well-organized study resources provided throughout the academic year due to the constant flow of information from external sources and their teachers.
This project identifies and attempts to fill in the gaps to alleviate the current challenges by developing an interface that caters to students’ specific needs in file storage and access, especially as they prepare for their examinations. The initiative’s main goal is to give students a platform to safely upload, store, and manage their study materials on a centralized server where they can access them. This approach will eventually simplify the arrangement of digital resources and provide students with a user-friendly method for handling their course materials.
This problem statement shows that there are various challenges students face throughout their learning journey and examinations due to the increasing rate of unpreparedness. The issue is attributed to the incapacity to store and fetch study materials, which impedes learning, increases needless stress, and reduces students’ productivity. Therefore, the goal of this project is to close this learning gap and present a feasible solution that will not only lessen their challenges but also improve the institutions’ overall academic outcomes and processes.
The suggested application will utilize Python and socket programming to develop a client-server application that will assist students in uploading their study materials to a central server, creating a safe, well-organized repository that is accessible from anywhere. In the application, students can easily upload, update, and download their study materials thanks to the client-side interface, which guarantees a smooth user experience. The server-side code manages file storage and retrieval, while the client-side provides an interface for user interaction (Henziger & Carlsson, 2019). This project is motivated by the realization that there is a consistent problem in the academic arena where institutions lack centralized file storage systems that are customized to meet students’ specific educational needs. The project will transform the institution’s approach to organizing their study materials and also provide user profiles where they can upload personal files, ultimately increasing learning efficiency and productivity in the classrooms.
Details About the Hardware and Software Used in The Project
This project was done using the CMD terminal on a Windows 10 machine, which handled the client execution prompts. Another tool used in the process was Visual Studio Code (VS Code), version 1.84, to run the server-side terminal. VS Code was the primary code editor containing the server.py and client.py files, which were stored in a similar file directory created by the command prompt. Also, the project featured the latest version of Python 3.12 software as the general-purpose language to execute and edit the Python scripts. Also, the VS Code terminal was used to view the server’s responses and progress, different from CMD, which handled the client-side segment of the code. Together, these software and hardware components collaborated in running the application by executing the project codes. Also, the VS Code file management tab assisted in the creation of new files for the development of projects and management of the working directory. The main file types used in the project were .txt files and .py files.  
Results and Discussions
Server-Side Code
On the server side of the project, the Python script uses TCP sockets, a vital component used in network communications to simulate a file transfer to the server (Tran & Bonaventure, 2019). The first step of the process is importing the `socket` module, a fundamental Python package for managing networking operations. Then, the application creates a foundation for creating and maintaining the server’s connections by initializing critical parameters such as the local IP address (IP), port number (PORT), buffer size (SIZE), and the data encoding format (FORMAT). 
The logic of the server is orchestrated by the (main) function, which instantiates the TCP socket using the IPV4, which addresses and binds the server to the provided port (Feng et al., 2021). Afterward, the server initiates a listening mode as it waits for new connections, after which two data structures (files_received), a dictionary, and (connected_clients), a list, are initiated. These data structures are critical to the server since they assist in the management of connected clients and the received file information.
 
In the next step of the process, the server initiates an infinite loop, which is typical of all server programs as they wait and manage incoming connections. In the iteration processes, the server is ready with an (accept) command to take an incoming connection request and retrieves the client address (add) and the object (conn). In the last step of the iteration, the script will print a message in case a new connection has been established or not. Following this, all of the important client data is kept in the (connected_clients) list, and the (files_received) dictionary contains details on the files that have been delivered. 
 
 Using the (recv) command, the server then gets the name of the file from the client’s end, opens it in read mode to extract the first line, and returns confirmations to the user (Tian & Gao, 2023). The client then sends the file information to the server. The process includes capturing the data that was received, reopening and locking the file, and giving the client a receipt of confirmation for the successful operation. The (files_received) dictionary has an appendix containing details about the uploaded file, which are stored for future access.
 
After that, the server shuts the file, ends the client’s connection, deletes the now-disconnected client’s data from the (connected_clients) list, and outputs a notice regarding the interruption.
 Lastly, the server produces the debug information, displaying the uploaded files and the corresponding clients’ present states. In the script, the try-except block handles unexpected keyboard interruptions and guarantees a proper server termination. 
 
This script allows administrators to track all the client interactions and follow through the file transfer processes in real-time while also transferring files from clients efficiently and providing extensive debugging tools (Sallow et al., 2020). It is the output’s duty on the terminal to confirm that the server can successfully run and manage interactions with clients and efficiently manage file transmissions. On the server output, the script must start by indicating that the server has started and is ready to receive connections. A client connection is established on port 60312 with IP address 192.168.0.101, which results in the receipt of document task2.txt and its contents. The script has configured the webserver to evaluate the incoming data output and pertinent debug information and indicates when the specified client is disconnected. Also, there is a dictionary that describes the received files and lists of client connections. When the server closes, it means that the client using the specified IP address has stopped communicating with the server in the interaction.
The entire Python script offers a concise and understandable way of creating a file transfer server with TCP sockets (Tran & Bonaventure, 2019). It also highlights the effective use of socket-based programming in Python by allowing efficient communication between the clients and a server. The modular structure of the code allows for its ease of comprehension and maintainability through the clearly specified functions and data structures. Also, there are efficient error management techniques like the try-except block, which are incorporated to increase the server’s dependability.
Server Side Output
The server-side output on the VS Code terminal reflects the sequential execution and interactions of the Python script intended for file transfer over TCP socket communication (Hassan et al., 2023). The first two messages on the terminal highlight the successful start of the server. (STARTING) means the server has been launched, and (LISTENING) means it is alert for new connections. Thus, the server is now actively waiting for incoming files on the predetermined IP address and port, in this case, ‘192.168.0.101’ and port 60312.  
After the successful connection with a client identified by the IP address 192.168.0.101 and port 60312, the server records the event with a (NEW CONNECTION) terminal output and a (192.168.0.101’, 60312) connected address. Afterward, there is a (RECV) result highlighting the receipt of the filename, which the server proceeds to get from the client after they upload it. Afterward, the (FILE CONTENT) section of the output should show the first line of task2.txt, which is printed as debug information by the script while being opened in read mode {r}. The script then reads the file, extracts the first line in the document, and highlights that it is “First, here is a schedule of the dates for our exams.”
On the terminal, there is the (RECV) message, which means “receiving the file data” and indicates that the server is in the process of getting the actual file from the client, which is the most fundamental step of the process after receiving the filename. For the entire process to succeed, it is primarily dependent on this phase. Therefore, when the server receives a message like (DISCONNECTED), it means that it has detected that the client has terminated the integration. This problem occurs due to network issues or intentional connection shutdown by the client. In the script, since the connection was successful, the server provides an update on the connected clients’ current status and the files it received, plus the debug data. 
After the disconnection of the client from the server, the linked device list is empty, signifying no active connections. Concurrently, details on the file (“task2.txt”) that was received from the now-disconnected client are contained in the files received dictionary as shown In the output with the listed study topics in the text file. At this stage, the debug information is an invaluable resource for monitoring server activity and troubleshooting any problems that could arise in the file transfer processes (Sugiyama et al., 2023). The output verifies that the server script handled the connection, got the file from the client, and controlled the disconnection event in an organized and watched fashion.
Client Side Code
The client side of the Python script allows for the efficient transfer of files using the TCP socket communication (Hassan et al., 2023). The first step of the code is setting up and initializing the terminal.    
This part of the client code, which was also written in VS Code, initializes the script by importing the necessary libraries and modules, such as (socket), whose role is to guarantee efficient networking and a (filedialog) from the (tkinter) library which allows for the graphical user interface (GUI) file dialog. The initial client code sets up variables for the port number, local IP address, buffer size, and data encoding format.    The {select_file()} function, defined in this subsection, allows an individual to pick a file by opening a GUI file window. It loads the chosen file path, launches the file dialog, makes the Tkinter framework root window hidden, and finally closes the Tkinter interface.
    
This section is the main part of the client-side script {main()} since it uses IPv4 addressing to create a TCP socket and provides the address ({client. connect(ADDR)}), which enables it to be ordered to connect to the server. The address of the chosen file is then obtained by the program from the user’s input via the GUI file box by applying the {select_file()} method. Afterward, the script prints an output, shuts down the client socket, and responds if the client cancels the file selection process. The information inside of the chosen file is then copied into the (data) variable when it is opened in binary mode for viewing through the (with open(file_path, “rb”) as file:}) command.    At this stage, the filename is prepared and sent to the server. Using ‘/’ as a separator, it then retrieves the name of the file from the directory path and transmits it in the desired format to the server through the (`client.send(filename.encode(FORMAT))}) command. After that, the server sends a message to the client.
    This step delivers the raw file data to the server through the ({client.send (data)}) command immediately after the filename has been transmitted (Pan et al., 2023). The document’s current state is then indicated in another notification stating that the client has received a notice from the server and outputs the information as debug material.
 
In the final step of the process, the script closes the client socket, indicating that it has completed the file transfer task and is ready for additional commands.
 
In the (if __name) stage, the script first determines if it happens to be executed as the main application, and if it is the primary one, it invokes the {main()} function to start the file transfer.
This client-side script connects to the server, opens a GUI file dialog, lets the user choose a file, reads its contents, transfers the filename and data to the server, gets acknowledgments, and ends the connection. This process highlights how the client and server communicate using a socket communication. The script facilitates error handling for situations such as aborted file selection and guarantees seamless communication between the client and the server (Tyagi, 2020). It also thoroughly analyzes every segment, highlighting its efficacy and clarity in explaining the processes’ inner workings.
Client-Side Output (CMD)
The client-side output in this project can be viewed through its execution on the Windows command prompt after passing a series of commands.  
The first step of the process was to change the current default machine directory to the project’s path using the {cd} command. The machine navigates to the directory containing the Python scripts file transfer project through this command.
    Afterward, the Python script (client.py) in the provided directory can be executed through the (Python client.py) command for execution and visibility of the file dialog box (Hosch et al., 2023). The code also starts the client-side script that connects to the server and transfers the file.
 
After running the code, it generates a GUI file dialog from which the student can select the file to upload to the server, which the Tkinter library facilitates on the client.py script.
    From the provided output message, the client output gives little details about the file’s contents. The message approves that the server has received the filename “task2.txt” from the client’s connection to the server. 
 
This line is an additional output message obtained from the server, verifying the successful reception of the file contents and confirming to the client that the file transfer procedure was completed successfully.
 
After the Python script has completed executing or running, the command prompt returns to the original directory as it awaits additional orders. In the CMD prompt, the output shows that the client connected to the server successfully, delivered the file task2.txt, got messages from the server confirming receipt of the file, and finished the file transfer procedure. The server’s messages reinforce the effective communication between the client and server throughout the file transfer process by being transparent about the server’s knowledge of the received filename and contents.
In conclusion, the file transfer project will assist students in monitoring their academic progress by accessing and uploading their documents to a central server. Institutions must develop the best mechanisms to ensure they ease students’ access to academic resources, which was this project’s primary aim. The project used socket and Python programming to link communication between the server and client interfaces to upload the files necessary for the student’s academic needs. Once implemented, this project can help many students have a central repository to access the information they need in their academic journey, boosting their learning outcomes. 



















References
Feng, X., Li, Q., Sun, K., Fu, C., & Xu, K. (2021). Off-path TCP hijacking attacks via the side channel of downgraded IPID. IEEE/ACM transactions on networking, 30(1), 409-422.
Gneezy, U., List, J. A., Livingston, J. A., Qin, X., Sadoff, S., & Xu, Y. (2019). Measuring success in education: The role of effort on the test itself. American Economic Review: Insights, 1(3), 291-308.
Hassan, G. M., Hussien, N. M., & Mohialden, Y. M. (2023). Python TCP/IP libraries: A Review. International Journal Papier Advance and Scientific Review, 4(2), 10-15.
Henziger, E., & Carlsson, N. (2019, December). The overhead of confidentiality and client-side encryption in cloud storage systems. In Proceedings of the 12th IEEE/ACM International Conference on Utility and Cloud Computing (pp. 209-217).
Hosch, R., Baldini, G., Parmar, V., Borys, K., Koitka, S., Engelke, M., ... & Nensa, F. (2023). FHIR-PYrate: a data science friendly Python package to query FHIR servers. BMC Health Services Research, 23(1), 734.
Laksana, D. N. L. (2020). Implementation of online learning in the pandemic covid-19: Student perception in areas with minimum internet access. Journal of Education Technology, 4(4), 502-509.
Pan, Y., Wu, D., Du, D., & Wang, H. (2023, July). Design and Performance Analysis of Protocol Conversion between 5G and Modbus TCP. In 2023 42nd Chinese Control Conference (CCC) (pp. 6262-6267). IEEE.
Sallow, A. B., Dino, H. I., Ageed, Z. S., Mahmood, M. R., & Abdulrazaq, M. B. (2020). Client/Server remote control administration system: Design and implementation. Int. J. Multidiscip. Res. Publ, 3(2), 7.
Sugiyama, S., Kobayashi, T., Shimari, K., & Ishio, T. (2022, March). JISDLab: A web-based interactive literate debugging environment. In 2022 IEEE International Conference on Software Analysis, Evolution and Reengineering (SANER) (pp. 497-501). IEEE.
Tian, Y. C., & Gao, J. (2023). Building TCP/IP Socket Applications. In Network Analysis and Architecture (pp. 501-540). Singapore: Springer Nature Singapore.
Tran, V. H., & Bonaventure, O. (2019, May). Beyond socket options: making the Linux TCP stack truly extensible. In 2019 IFIP Networking Conference (IFIP Networking) (pp. 1-9). IEEE.
Tyagi, A. (2020). Tcp/ip protocol suite. Int. J. Sci. Res. Comput. Sci. Eng. Inf. Technol, 6(4), 59-71.

 
 

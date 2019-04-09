# Logs Analysis
This is an internal reporting tool to gain the insight on the following questions:
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

## Getting started
### Prerequisites
You need to install psycopg2 to run the code.
```
$ pip install psycopg2
```

### Installing
The program can be run on the virtual machine by using such tools as Vagrant and VirtualBox.
Here are some tips to install these tools and set up for your environment.

#### Installing VirtualBox
You can download the latest version of VirtualBox from [here](https://www.virtualbox.org/wiki/Downloads). As of January 2019, you can get VirtualBox 6.0 which is also supported by the current version of Vagrant (2.2.3)

Once you download it, install the platform package on your operating system. You do not need to launch the app itself since it is taken care of by Vagrant.


#### Installing Vagrant
You can download the latest version of Vagrant from [here](https://www.vagrantup.com/downloads.html). As of January 2019, you can get Vagrant 2.2.3 which supports the current version of VirtualBox (6.0).

Once you download it, install the platform package on your operating system.

#### Configure your Vagrant and access to the virtual machine
After you installed both VirtualBox and Vagrant, you should clone this [repositry](https://github.com/udacity/fullstack-nanodegree-vm) to get the pre-set configuration file for your virtual machine.
Then you use `cd` command to move into **vagrant** directory which is located in the directory you cloned.

You run the command `vagrant up` (it may take a while to initially set up the environment), then run the command `vagrant ssh`.
If you see a shell prompt that starts with the word `vagrant`, it means that you successfully logged in your virtual machine!

Inside your virtual machinde, run the comomand `cd` to move the directory to **/vagrant** where the files can be shared with your local computer.

### Importing the data into the database
The dataset we use for this code is downloaded from [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip).

You should upnzip the downloaded file, and find the file named `newsdata.sql`. Put the file into `vagrant` directly, in which files are shared between your local computer and virtual machine.

To load the data, change the directry to `vagrant` by using `cd`, then run the command as below:
```
$ psql -d news -f newsdata.sql
```
Running this command will connect to your installed database server and execute the SQL commands in the downloaded file, creating tables and populating them with data.


### Requirement of creating new views
In order to run the program appropriately, you need to create new views.

To access the database, run the following command.
```
$ psql news
```

To create views neccesary for running the code, run the following SQL commands.

```
create view articles_pv as select path, count (*) as views from log where status = '200 OK' group by path;
```
```
create view errors as select date(time) as date, count (*) as errors from log where status = '404 NOT FOUND’ group by date;
```
```
create view total_access as select date(time) as date, count (*) as access from log group by date;
```

### Running the code
To run the code, you may use the following comand.
```
$python3 logs_analysis.py
```

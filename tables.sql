DROP TABLE IF EXISTS clients;
DROP TABLE IF EXISTS publisher;
DROP TABLE IF EXISTS Books;
DROP TABLE IF EXISTS staff;
DROP TABLE IF EXISTS history;
DROP TABLE IF EXISTS Reserve;
DROP TABLE IF EXISTS Maintains;
DROP TABLE IF EXISTS Reports;
DROP TABLE IF EXISTS Tracks;
DROP TABLE IF EXISTS accessHistory;

--client table aka users table
create table clients
(
    clientID        integer primary key not Null,
    name            varchar(20),
    username        varchar(20),
    password        varchar(20)
);

--publisher table
create table publisher(
    publisher_id    varchar(5), 
    name            varchar(20) not null,
    email           varchar(20) not null,
    primary key (publisher_id)
);

--books table
create table Books(
    ISBN            varchar(13),
    title           varchar(20),
    author          varchar(20),
    genre           varchar(10),
    --publisher_id    varchar(5),
    page_count      varchar(4),
    id              integer not null,
    primary key (ISBN)--,
    --foreign key (publisher_id) references publisher
);

--staff table
create table staff(
    sID           integer not NULL,
    name          varchar(20),
    username      varchar(20),
    password      varchar(20),
    primary key (sID)
);

--history of clients table
create table history(
    history_id      Integer not NULL,
    clientID        Integer,
    orders          varchar(40),
    primary key (history_id),
    foreign key (clientID) references clients (clientID)
);

--reserve book table
create table Reserve(
    ReserveID   integer Not Null,
    clientID    text,
    bookID      text,
    status      varchar(40),
    primary key (ReserveID),
    foreign key (BookID) REFERENCES Books (ISBN),
    foreign key (clientID) References clients (clientID)
);

--keep track of by staff
create table Maintains(
    quantity     numeric(4,0),
    bookID       varchar(13),
    PRIMARY key (bookID),
    foreign key (bookID) references Books (ISBN) on delete cascade
);

-- Reports generated for staff only
create table Reports(
    RepID    integer not Null,
    clientID Integer,
    BookID   varchar(13),
    status   varchar(40),
    PRIMARY key (bookID,RepID),
    foreign key (BookID) REFERENCES Books (ISBN),
    foreign key (clientID) References clients (clientID),
    foreign key (status) REFERENCES Reserve (status)
);

create table tracks(
    staffID     Integer,
    clientID    Integer,
    foreign key (clientID) References clients (clientID),
    foreign key (staffID)  References staff (sID)
);

create table accessHistory(
    staffId     Integer,
    historyID   Integer,
    foreign key (staffId)  References staff (sID),
    foreign key (historyID)  References history (history_id)
);

delete from clients;
delete from staff;
delete from publisher;
delete from Books;
delete from Maintains;
delete from Reserve;
delete from tracks;
delete from Reports;
delete from history;
delete from accessHistory;
--create insert data to input data into it
--clients and their username and data
--client data
INSERT or REPLACE into clients (name,username,password) values ('Nirmith','nirmith','nirmith');
insert or REPLACE into clients (name,username,password) values ('JayYellow','JayInTheBox','JayYeet');
--SELECT * from clients;

--staff data
Insert or Replace into staff (name,username,password) values ('jack','jack32','J@ck');
Insert or Replace into staff (name,username,password) values ('jill','jill45','J1ll');
Insert or Replace into staff (name,username,password) values ('hill','hill31','H1ll');
--Select * from staff;

--Insert or replace into publisher
Insert or replace into publisher (publisher_id,name,email) values ('pub1','J. W. Arrowsmith','sales@arrowsmith.co.uk');
Insert or replace into publisher (publisher_id,name,email) values ('pub2','Bloomsbury Publishing','contact@bloomsbury.com');
Insert or replace into publisher (publisher_id,name,email) values ('pub3','Allen and Unwin','MHoy@allenandunwin.com');
--Select * from publisher;

--books data
--Insert or Replace into Books (ISBN,title,author,genre,publisher_id,page_count) values ('0199537976','Three Men In A Boat','Jerome K. Jerome','adventure','pub1','185');
--Insert or Replace into Books (ISBN,title,author,genre,publisher_id,page_count) values ('1510096004','Idle Thoughts of an Idle Fellow','Jerome K. Jerome','humor','pub1','210');
--Insert or Replace into Books (ISBN,title,author,genre,publisher_id,page_count) values ('1515252604','The New Utopia','Jerome K. Jerome','fiction','pub1','190');
--Insert or Replace into Books (ISBN,title,author,genre,publisher_id,page_count) values ('0590353403','Harry Potter and the Sorcerer''s / Philosopher''s Stone','J.K.Rowling','adventure','pub2','309');
--Insert or Replace into Books (ISBN,title,author,genre,publisher_id,page_count) values ('0439064864','Harry Potter and the Chamber of Secrets','J.K. Rowling','adventure','pub2','251');
--Insert or Replace into Books (ISBN,title,author,genre,publisher_id,page_count) values ('0747542155','Harry Potter and the Prisoner of Azkaban','J.K. Rowling','fiction','pub2','317');
--Insert or Replace into Books (ISBN,title,author,genre,publisher_id,page_count) values ('9780261102','The Hobbit','JRR Tolkein','adventure','pub3','310');
--Insert or Replace into Books (ISBN,title,author,genre,publisher_id,page_count) values ('0261102354','The Fellowship of the Ring','JRR Tolkein','adventure','pub3','423');
--Insert or Replace into Books (ISBN,title,author,genre,publisher_id,page_count) values ('0345339738','The Return of the King','JRR Tolkein','adventure','pub3','416');

Insert or Replace into Books (ISBN,title,author,genre,page_count,id) values ('0199537976','Three Men In A Boat','Jerome K. Jerome','adventure','185',1);
Insert or Replace into Books (ISBN,title,author,genre,page_count,id) values ('1510096004','Idle Thoughts of an Idle Fellow','Jerome K. Jerome','humor','210',2);
Insert or Replace into Books (ISBN,title,author,genre,page_count,id) values ('1515252604','The New Utopia','Jerome K. Jerome','fiction','190',3);
Insert or Replace into Books (ISBN,title,author,genre,page_count,id) values ('0590353403','Harry Potter and the Sorcerer''s / Philosopher''s Stone','J.K.Rowling','adventure','309',4);
Insert or Replace into Books (ISBN,title,author,genre,page_count,id) values ('0439064864','Harry Potter and the Chamber of Secrets','J.K. Rowling','adventure','251',5);
Insert or Replace into Books (ISBN,title,author,genre,page_count,id) values ('0747542155','Harry Potter and the Prisoner of Azkaban','J.K. Rowling','fiction','317',6);
Insert or Replace into Books (ISBN,title,author,genre,page_count,id) values ('9780261102','The Hobbit','JRR Tolkein','adventure','310',7);
Insert or Replace into Books (ISBN,title,author,genre,page_count,id) values ('0261102354','The Fellowship of the Ring','JRR Tolkein','adventure','423',8);
Insert or Replace into Books (ISBN,title,author,genre,page_count,id) values ('0345339738','The Return of the King','JRR Tolkein','adventure','416',9);
--Select * from Books;

--adding data for quantity of each book
insert or Replace into Maintains (quantity,bookID) values (20,'0199537976');
insert or Replace into Maintains (quantity,bookID) values (10,'1510096004');
insert or Replace into Maintains (quantity,bookID) values (30,'1515252604');
insert or Replace into Maintains (quantity,bookID) values (0,'0590353403');
insert or Replace into Maintains (quantity,bookID) values (7,'0439064864');
insert or Replace into Maintains (quantity,bookID) values (20,'0747542155');
insert or Replace into Maintains (quantity,bookID) values (2,'9780261102');
insert or Replace into Maintains (quantity,bookID) values (10,'0261102354');
insert or Replace into Maintains (quantity,bookID) values (15,'0345339738');
--Select * from Maintains;

--adding temporary data for reserving a book for EXISTING users
insert or replace into Reserve (clientID,BookID,status) values (1,'0199537976','borrowed');
insert or replace into Reserve (clientID,BookID,status) values (2,'1515252604','borrowed');
insert or replace into Reserve (clientID,BookID,status) values (1,'1515252604','returned');
--Select * from Reserve;

--adding temporary TRACKING data for EXISTING USERS AND STAFF
insert or replace into tracks (staffID,clientID) values (1,1);
insert or replace into tracks (staffID,clientID) values (2,1);
insert or replace into tracks (staffID,clientID) values (3,1);
insert or replace into tracks (staffID,clientID) values (1,2);
insert or replace into tracks (staffID,clientID) values (2,2);
insert or replace into tracks (staffID,clientID) values (3,2);
--select * from tracks;

--Reports Generated
Insert or replace into Reports (RepID,clientID,BookID,status) values (01,1,'0199537976','borrowed');
Insert or replace into Reports (RepID,clientID,BookID,status) values (02,2,'1515252604','borrowed');
--Select * from Reports;

--history value
insert or replace into history (clientID,orders) values (1,'0199537976 borrowed');
--Select * from history;

--access history 
insert or replace into accessHistory (staffId,historyID) values (1,1);
--Select * from accessHistory;
create type user_role as enum ('student', 'teacher');

create table classes (
    id serial primary key,
    name varchar(3) unique not null
);

create table users (
    id serial primary key,
    first_name varchar(50) not null,
    last_name varchar(50) not null ,
    email varchar(50) not null unique,
    password_hash varchar(255) not null,
    role user_role not null,
    class_id int,
    foreign key (class_id) references classes(id) on delete set null
);

create table subjects (
    id serial primary key,
    name varchar(30) not null
);

create table grades (
    id serial primary key,
    grade int not null,
    date date not null,
    subject_id int,
    teacher_id int,
    student_id int,
    foreign key (subject_id) references subjects(id) on delete cascade,
    foreign key (student_id) references users(id) on delete cascade,
    foreign key (teacher_id) references users(id) on delete cascade
);

create table class_subjects (
    id serial primary key,
    class_id int,
    subject_id int,
    foreign key (class_id) references classes(id) on delete cascade,
    foreign key (subject_id) references subjects(id) on delete cascade
);

create table teacher_subjects (
    id serial primary key,
    teacher_id int,
    subject_id int,
    foreign key (teacher_id) references users(id) on delete cascade,
    foreign key (subject_id) references subjects(id) on delete cascade
)
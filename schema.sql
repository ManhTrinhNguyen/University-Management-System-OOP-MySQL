# A many-to-many relationship is when multiple records in one table are related to multiple records in another table. This relationship usually requires a junction table (also called a bridge table or association table) to resolve the relationship.


#  Each department can have multiple professors and students (one-to-many).
CREATE TABLE departments (
    department_id INT PRIMARY KEY AUTO_INCREMENT,
    department_name VARCHAR(100)
);

# Professors: Professors can teach multiple courses (one-to-many), and they can supervise multiple research projects.
# Inheritance: Professors and students are both people (inherit from a base class Person).
CREATE TABLE people (
    person_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    email VARCHAR(100),
    role VARCHAR(50), -- 'professor' or 'student'
    department_id INT,
    FOREIGN KEY (department_id) REFERENCES departments(department_id)
);

# Courses: A course is taught by one professor, but many students can be enrolled (many-to-many).
CREATE TABLE courses (
    course_id INT PRIMARY KEY AUTO_INCREMENT,
    course_name VARCHAR(100),
    professor_id INT,
    FOREIGN KEY (professor_id) REFERENCES people(person_id) -- Professors are stored in the 'people' table
);

# Students: Students can enroll in multiple courses (many-to-many), and a student can be involved in one or more research projects (many-to-many).
# Juntion table of students and course (Many to Many)
CREATE TABLE students_courses (
    student_id INT,
    course_id INT,
    FOREIGN KEY (student_id) REFERENCES people(person_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id),
    PRIMARY KEY (student_id, course_id)
);

# Research Projects: A research project can have multiple students and one lead professor.
CREATE TABLE research_projects (
    project_id INT PRIMARY KEY AUTO_INCREMENT,
    project_name VARCHAR(100),
    lead_professor_id INT,
    FOREIGN KEY (lead_professor_id) REFERENCES people(person_id)
);

# Junction table of projects and students (Many to Many)
CREATE TABLE projects_students (
    project_id INT,
    student_id INT,
    FOREIGN KEY (project_id) REFERENCES research_projects(project_id),
    FOREIGN KEY (student_id) REFERENCES people(person_id),
    PRIMARY KEY (project_id, student_id)
);
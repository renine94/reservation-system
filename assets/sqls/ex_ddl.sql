CREATE TABLE "User" (
  "id" integer PRIMARY KEY,
  "email" varchar,
  "username" varchar,
  "phone_number" varchar,
  "is_active" bool,
  "is_staff" bool,
  "is_superuser" bool,
  "created_at" timestamp,
  "updated_at" timestamp
);

CREATE TABLE "Exam" (
  "id" integer PRIMARY KEY,
  "title" varchar,
  "description" text,
  "max_capacity" integer,
  "current_capacity" integer,
  "reservation_started_at" timestamp,
  "reservation_ended_at" timestamp,
  "started_at" timestamp,
  "ended_at" timestamp
);

CREATE TABLE "Reservation" (
  "id" integer PRIMARY KEY,
  "user_id" interger,
  "exam_id" integer,
  "status" enum,
  "created_at" timestamp,
  "updated_at" timestamp
);

ALTER TABLE "Reservation" ADD FOREIGN KEY ("user_id") REFERENCES "User" ("id");

ALTER TABLE "Reservation" ADD FOREIGN KEY ("exam_id") REFERENCES "Exam" ("id");

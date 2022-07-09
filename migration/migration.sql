-- Create table users
DROP TABLE IF EXISTS public.users;
CREATE TABLE public.users
(
    id              INT PRIMARY KEY,
    email           VARCHAR(50) UNIQUE NOT NULL,
    hashed_password VARCHAR(50)        NOT NULL,
    is_active       BOOLEAN            NOT NULL
);

-- Create table items
DROP TABLE IF EXISTS public.items;
CREATE TABLE public.items
(
    id          INT PRIMARY KEY,
    title       VARCHAR(50) NOT NULL,
    description VARCHAR(50) NOT NULL,
    owner_id    INT UNIQUE
);

-- Add Foreign Key
ALTER TABLE public.users
    ADD CONSTRAINT user_id_fk FOREIGN KEY (id) REFERENCES public.items (owner_id);

-- Indexing
CREATE INDEX title_idx ON public.items (title);
CREATE INDEX description_idx ON public.items (description);
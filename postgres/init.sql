CREATE TABLE public.user
(
    id      VARCHAR(255) NOT NULL,
    name    VARCHAR(255) NOT NULL,
    email   VARCHAR(255) NOT NULL,
    address VARCHAR(255) NOT NULL
);

CREATE TABLE public.payment
(
    id      VARCHAR(255) NOT NULL,
    user_id VARCHAR(255) NOT NULL,
    amount  INT          NOT NULL
);

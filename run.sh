#!/bin/bash
export POSTGRES_URI="postgresql://khangdx:abcd1234@localhost:5432/test"

uvicorn server:app --reload
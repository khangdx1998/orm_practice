#!/bin/bash
export POSTGRES_URI="postgresql://khangdx:abcd1234@localhost:5432/test"
export API_KEY="abacdasdf-123242"

uvicorn server:app --reload
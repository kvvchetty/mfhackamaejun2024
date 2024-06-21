docker build -t p1step2 .
docker run -v "$(pwd)/data:/app/input" -v "$(pwd)/data:/app/output" p1step2 step1outputfile.xlsx rentstab.xlsx outputfile.xlsx

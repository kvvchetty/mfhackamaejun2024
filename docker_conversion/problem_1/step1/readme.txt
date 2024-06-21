docker build -t p1step1 .
docker run -v "$(pwd)/data:/app/input" -v "$(pwd)/data:/app/output" p1step1 inputfile.xlsx outputfile.xlsx

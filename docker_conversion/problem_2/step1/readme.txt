docker build -t p2step1 .
docker run -v "$(pwd)/data:/app/input" -v "$(pwd)/data:/app/output" p2step1 property_file.xlsx section8.xlsx outputfile.xlsx

mkdir -p build
# Git clone the project
git clone git@github.com:nilportugues/production-api-translate-python.git build
 
# Generate release tarball
cd build/src/
python setup.py sdist
cd ..
cd ..

# save somewhere the build at: 
mv ./build/src/dist/translate_api-0.1.tar.gz ./docker

rm -rf build

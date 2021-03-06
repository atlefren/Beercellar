DB=beercellar.sql
APP=beerlist
tmpdate=$(date "+%Y%m%d-%H%M%S")

echo "+ Dumping django project database to fixture DUMP-${tmpdate}.json ..." &&\
python manage.py dumpdata $APP --format='json' --indent=4 --verbosity=1 > datadumps/DUMP-${tmpdate}.json &&\
echo '+ Backing up sqlite binary store...' &&\
cp $DB $DB.bk &&\
echo '+ Rebuilding database structure from model defs...' &&\

read "wait"

python manage.py reset $APP &&\
echo "+ Reloading project data from fixture dump DUMP-${tmpdate}.json ..." &&\
python manage.py loaddata datadumps/DUMP-${tmpdate}.json
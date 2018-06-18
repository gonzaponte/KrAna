for i in $@
do
    for template in Kr_selection.ipynb Kr_lifetime_map_builder.ipynb Kr_geometry_map_builder.ipynb Kr_plots.ipynb
    do
        NB=${template%.*}_${i}.ipynb
        cp ${template} ${NB}
        perl -pi -e 's/XXX_RUN_NUMBER_XXX/'"$i"'/g' ${NB}
        jupyter nbconvert --ExecutePreprocessor.timeout=None --to notebook --execute ${NB} --output ${NB} --allow-errors
    done
done
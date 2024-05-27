export PYTHONPATH=${PYTHONPATH}:/work/maceQEq_main/mace-tools
export PYTHONPATH=${PYTHONPATH}:/work/maceQEq_main/graph_longrange

python /work/maceQEq_main/mace-tools/scripts/eval_configs.py --configs="NaCltrain.xyz" --model="Polarizable.model" --output="pol_will_res.xyz" --device="cuda" 

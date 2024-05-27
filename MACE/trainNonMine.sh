export PYTHONPATH=${PYTHONPATH}:/work/maceQEq_main/mace-tools
export PYTHONPATH=${PYTHONPATH}:/work/maceQEq_main/graph_longrange

python /work/maceQEq_main/mace-tools/scripts/will_train.py --name="Polarizable" --train_file="NaCltrain.xyz" --valid_file="NaClval.xyz" --batch_size=10 --valid_batch_size=10 --config_type_weights='{"Default":1.0}' --E0s='{11: -4421.77421255, 17:-12577.38265088}' --model="Polarizable" --hidden_irreps='64x0e' --r_max=4.0 --max_num_epochs=150 --device=cuda --loss="atomic_multipoles" --formal_charges_from_data --lr=0.001 --error_table="DensityCoefficientsRMSE" --energy_weight=10.0 --forces_weight=100.0 --restart_latest --atomic_multipoles_key="atomic_multipoles" 

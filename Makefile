svg_optimize:
	python3 -m svg_handler.svg_subplot
	sleep 5

vpype_multi: svg_optimize
	vpype \
    forfile "vpype/input/*.svg" \
      read --layer %_i+1% %_path% \
    end \
    write vpype/output/output.svg

vpype_fab: vpype_multi
	vpype read vpype/output/output.svg layout -m 0.5cm -l -h center -v center 7x5in write vpype/output/final_for_axi.svg

vpype_fab_big: vpype_multi
	vpype read vpype/output/output.svg layout -m 1cm -l -h center -v center 8.25x6in write vpype/output/final_for_axi.svg

vpype_fab_extra: vpype_multi
	vpype read vpype/output/output.svg layout -m 1cm -l -h center -v center 12x9in write vpype/output/final_for_axi.svg

vpype_sqr: vpype_multi
	vpype read vpype/output/output.svg layout -m 1cm -l -h center -v center 20x20cm write vpype/output/final_for_axi.svg

vpype_canson: vpype_multi
	vpype read vpype/output/output.svg layout -m 1cm -l -h center -v center 8.3x5.8in write vpype/output/final_for_axi.svg

vpype_fab_big_sqr: vpype_multi
	vpype read vpype/output/output.svg layout -m 2cm -l -h center -v center 8.25x6in write vpype/output/final_for_axi.svg

vpype_a5_2:
	vpype read input.svg rotate -- -1 trim 0.3in 0.3in penwidth 0.05mm layout -m 1cm -l -h center -v center 8.3x5.8in write output.svg

vpype_a5:
	vpype read input3.svg layout -m 1cm -l -h center -v center 8.3x5.8in write output3.svg



vpype_a4:
	vpype read input.svg scaleto 5.8in 5.8in trim 0.4in 0.4in penwidth 0.5mm layout -m 1cm -l -h center -v center a4 write output.svg

vpype_opt:
	vpype read input.svg splitall linemerge --tolerance 0.5mm write output_optimised.svg

dedup:
	vpype read input.svg deduplicate -t 0.1mm write dedup_output.svg
	vpype read dedup_output.svg linemerge -t 0.1mm linesort layout --landscape a5 write dedup_full_output.svg


vpype_layer:
	vpype read full.svg forlayer write output_%_name%.svg end

motor_down:
	axicli -m manual -M disable_xy
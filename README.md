# arxiv-term
A simple Terminal Arxiv viewer

Just download the .py file and run
If you want to directly run from terminal you might want to give it execution access using 

```chmod +x arxiv.py```


For Eg: If you are in the same folder as the file  ```./arxiv.py -h``` should give you all the necessary details.

Only few physics fields have been added now, More will be added later.
    usage: arxiv [-h]
                [--astro_ph | --cond_mat | --gr_qc | --hep_ex | --hep_lat | --hep_ph | --hep_th]
                [--new | --recent] [-r] [-d DOWNLOAD] [-v VIEW]

    optional arguments:
    -h, --help            show this help message and exit
    --astro_ph            High Energy Physics Theory
    --cond_mat            Condensed Matter Physics
    --gr_qc               General Relativity and Cosmology
    --hep_ex              High Energy Physics Experiment
    --hep_lat             High Energy Physics Lattice
    --hep_ph              High Energy Physics Phenomenology
    --hep_th              High Energy Physics Theory
    --new                 From /<department>/new
    --recent              From /<department>/recent
    -r, --replacement     Include Replacement papers in new
    -d DOWNLOAD, --download DOWNLOAD
                            Download the pdf of the given arxiv ID
    -v VIEW, --view VIEW  View the details of the given arxiv ID

Querying will be added soon.

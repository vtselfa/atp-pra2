spec2006 = {
	"astar" : {
		"exe" : "astar_base.i386",
		"args" : "rivers.cfg",
		"cwd" : "benchmarks/spec2006/473.astar",
	},

	"bwaves" : {
		"exe" : "bwaves_base.i386",
		"cwd" : "benchmarks/spec2006/410.bwaves",
	},

	"bzip2" : {
		"exe" : "bzip2_base.i386",
		"args" : "input.source 280",
		"cwd" : "benchmarks/spec2006/401.bzip2",
	},

	"cactusADM" : {
		"exe" : "cactusADM_base.i386",
		"args" : "benchADM.par",
		"cwd" : "benchmarks/spec2006/436.cactusADM",
	},

	"calculix" : {
		"exe" : "calculix_base.i386",
		"args" : "-i hyperviscoplastic",
		"cwd" : "benchmarks/spec2006/454.calculix",
	},

	"dealII" : {
		"exe" : "dealII_base.i386",
		"args" : "23",
		"cwd" : "benchmarks/spec2006/447.dealII",
	},

	"gamess" : {
		"exe" : "gamess_base.i386",
		"stdin" : "triazolium.config",
		"cwd" : "benchmarks/spec2006/416.gamess",
	},

	"gcc" : {
		"exe" : "gcc_base.i386",
		"args" : "166.i -o 166.s",
		"cwd" : "benchmarks/spec2006/403.gcc",
	},

	"GemsFDTD" : {
		"exe" : "GemsFDTD_base.i386",
		"cwd" : "benchmarks/spec2006/459.GemsFDTD",
	},

	"gobmk" : {
		"exe" : "gobmk_base.i386",
		"args" : "--quiet --mode gtp",
		"stdin" : "trevord.tst",
		"cwd" : "benchmarks/spec2006/445.gobmk",
	},

	"gromacs" : {
		"exe" : "gromacs_base.i386",
		"args" : "-silent -deffnm gromacs -nice 0",
		"cwd" : "benchmarks/spec2006/435.gromacs",
	},

	"h264ref" : {
		"exe" : "h264ref_base.i386",
		"args" : "-d sss_encoder_main.cfg",
		"cwd" : "benchmarks/spec2006/464.h264ref",
	},

	"hmmer" : {
		"exe" : "hmmer_base.i386",
		"args" : "--fixed 0 --mean 500 --num 500000 --sd 350 --seed 0 retro.hmm",
		"cwd" : "benchmarks/spec2006/456.hmmer",
	},

	"lbm" : {
		"exe" : "lbm_base.i386",
		"args" : "3000 reference.dat 0 0 100_100_130_ldc.of",
		"cwd" : "benchmarks/spec2006/470.lbm",
	},

	"leslie3d" : {
		"exe" : "leslie3d_base.i386",
		"stdin" : "leslie3d.in",
		"cwd" : "benchmarks/spec2006/437.leslie3d",
	},

	"libquantum" : {
		"exe" : "libquantum_base.i386",
		"args" : "1397 8",
		"cwd" : "benchmarks/spec2006/462.libquantum",
	},

	"mcf" : {
		"exe" : "mcf_base.i386",
		"args" : "inp.in",
		"cwd" : "benchmarks/spec2006/429.mcf",
	},

	"milc" : {
		"exe" : "milc_base.i386",
		"stdin" : "su3imp.in",
		"cwd" : "benchmarks/spec2006/433.milc",
	},

	"namd" : {
		"exe" : "namd_base.i386",
		"args" : "--input namd.input --iterations 38 --output namd.out",
		"cwd" : "benchmarks/spec2006/444.namd",
	},

	"omnetpp" : {
		"exe" : "omnetpp_base.i386",
		"args" : "omnetpp.ini",
		"cwd" : "benchmarks/spec2006/471.omnetpp",
	},

	"perlbench" : {
		"exe" : "perlbench_base.i386",
		"args" : "checkspam.pl 2500 5 25 11 150 1 1 1 1",
		"cwd" : "benchmarks/spec2006/400.perlbench",
	},

	"povray" : {
		"exe" : "povray_base.i386",
		"args" : "SPEC-benchmark-ref.ini",
		"cwd" : "benchmarks/spec2006/453.povray",
		"Stdout" : "povray.out",
	},

	"sjeng" : {
		"exe" : "sjeng_base.i386",
		"args" : "train.txt",
		"cwd" : "benchmarks/spec2006/458.sjeng",
	},

	"soplex" : {
		"exe" : "soplex_base.i386",
		"args" : "-m3500 ref.mps",
		"cwd" : "benchmarks/spec2006/450.soplex",
	},

	"sphinx3" : {
		"exe" : "sphinx3_base.i386",
		"args" : "ctlfile . args.an4",
		"cwd" : "benchmarks/spec2006/482.sphinx3",
	},

	"tonto" : {
		"exe" : "tonto_base.i386",
		"cwd" : "benchmarks/spec2006/465.tonto",
	},

	"wrf" : {
		"exe" : "wrf_base.i386",
		"cwd" : "benchmarks/spec2006/481.wrf",
	},

	"xalancbmk" : {
		"exe" : "xalancbmk_base.i386",
		"args" : "-v t5.xml xalanc.xsl",
		"cwd" : "benchmarks/spec2006/483.xalancbmk",
	},

	"zeusmp" : {
		"exe" : "zeusmp_base.i386",
		"cwd" : "benchmarks/spec2006/434.zeusmp",
	},
}


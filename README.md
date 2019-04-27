# How To Use 

Start with a k8s template file you want to convert to a helm chart.

Run

		$ ./run.sh /path/to/your/template/file

# What Does It Do?

Inside your cloned repository, `run.sh` will create a `charts` folder. It then calls `helm create ./charts/<base name of your template file>` to get a helm chart started in the correct format. Finally, `run.sh` calls `kube2helm.py -f /path/to/your/template/file`, which parses the template file YAML and breaks out each object into its own helm chart template file inside `./charts/<your new chart>/templates/` with the filename format `<object type>_<object name>.yml`. 

# What Else Should It Do?

There are other things that need to happen to get a working helm chart from a k8s template. Many of these can be done programmatically with Python and its handling of the content with `pyyaml`.

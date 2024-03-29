# Steps to Use Self hosted runner
* in your actions.yml file use the label self hosted "runs-on: self-hosted"

# than follow the steps on the instance or your local machine(to use your local as a VM)

* Go to the repo setting> click on actions --> click on runners ->> New Self hosted runner
* follow the steps given run the 

```sh
./run.sh
```
# you will see "2024-01-03 06:01:47Z: Listening for Jobs"
![Screenshot](/src/image.png)

* NOTE the runner you create is specific for that repo


## Comparing with Jenkins 

### Advantages of GitHub Actions over Jenkins

- Hosting: Jenkins is self-hosted, meaning it requires its own server to run, while GitHub Actions is hosted by GitHub and runs directly in your GitHub repository.

- User interface: Jenkins has a complex and sophisticated user interface, while GitHub Actions has a more streamlined and user-friendly interface that is better suited for simple to moderate automation tasks.

- Cost: Jenkins can be expensive to run and maintain, especially for organizations with large and complex automation needs. GitHub Actions, on the other hand, is free for open-source projects and has a tiered pricing model for private repositories, making it more accessible to smaller organizations and individual developers.

### Advantages of Jenkins over GitHub Actions

- Integration: Jenkins can integrate with a wide range of tools and services, but GitHub Actions is tightly integrated with the GitHub platform, making it easier to automate tasks related to your GitHub workflow.

In conclusion, Jenkins is better suited for complex and large-scale automation tasks, while GitHub Actions is a more cost-effective and user-friendly solution for simple to moderate automation needs.


# USING ACT (github actions locally )
* note : you cant use self hosted when using act
* we can check the actions workflow locally by using act though we dont have a good UI like on 
* github but still its good for running workflows locally
 
 https://github.com/nektos/act

 ![Alt text](/src/act.png)

 ```sh
#bydefault runs on push event
act 

#list all actions for all events
act -l 

#run on spefic event
act pull request

#run a spefici job
act -j test 

#list the actions for a specific job
act -j test -l
 ```
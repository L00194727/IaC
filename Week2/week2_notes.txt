# Week2 Notes  

First, I downloaded ISOs for both Ubuntu 24.04 Desktop and Server and verified they installed successfully by running them and ensuring they logged in. 

## Snapshots

When a snapshot is made, a delta disk file (.vmdk) is made, and a memory file is created (.vmem) also a (.vmsd) file which is a text file describing the snapshot hierarchy.
Snapshots are like pictures of the OS at a current time if I install a program, on the snapshot and then revert to the snapshot the program won’t be there anymore. They are suppose to be short-lived, we use them before install patches or upgrading the system, we then test the system if everything runs ok we then delete the snapshots.

After deletion the created files for the snapshot are removed.

## Clones

**Full clone** – The created child is a independent copy of the parent. Both parent and child can use the network and have different MAC addresses
**Linked clone** – A copy called a child clone is created from a parent clone, it uses delta file to track changes from the parent to the child. If the parent gets deleted the child will stop working. Both parent and child can use the network and have different MAC addresses

## Networking

**NAT Network** - Internet access without needing to configure it, allows you to exposes VM services to outside world by port forwarding, and external computers cant directly access the VM. The host can ping the Virtual Machine because they are both on VMnet8

**Host Only Network** – In this configuration the VM cant access the internet it can only communicate with the host computer and other Virtual Machines on the hosts network. It allows complete isolation from internet and is useful for local development and testing.


**Bridged Network** -  Gives VM direct access to Network Card allowing it direct access to physical network like it was a real machine. Its useful for testing real network interactions.

**LAN Segment** - Creates a completely isolated Virtual Network, where VMs can only communicate with other VMs in the Lan Segment

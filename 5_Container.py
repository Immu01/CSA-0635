def container_loader(items,container_volume):
    items.sort(key=lambda x:x[1]/x[0],reverse=True)
    containers=[]
    current_container={'items':[],'remaining_volume':container_volume}
    for item in items:
        if item[0]<=current_container['remaining_volume']:
            current_container['items'].append(item)
            current_container['remaining_volume']-=item[0]
        else:
            containers.append(current_container)
            current_container={'items':[item],'remaining_volume':container_volume}
    containers.append(current_container)
    return containers
def print_containers(containers):
    print("\nContainer Loading Result :\n")
    for i, container in enumerate(containers):
        print(f"\nContainer {i+1} :")
        total_weight=0
        total_volume=0
        for item in container['items']:
            print(f"Item {item}:weight= {item[0]},volume= {item[1]}")
            total_weight+=item[0]
            total_volume+=item[1]
        print(f"Total weight: {total_weight},Total volume: {total_volume}")
        print()
if __name__=="__main__":
    items=[(10,2),(5,3),(8,1),(4,2),(6,3)]
    container_volume=5
    containers=container_loader(items,container_volume)
    print_containers(containers)
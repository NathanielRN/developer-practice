#!/usr/bin/python3

from typing import List, Dict
from enum import Enum

# Example input:
# Projects A, B, C, D, E , F
# Dependencies: (a, d), (f, b), (b, d), (f, a), (d, c)
# Output: f, e, a, b, d, c


class ProjectStatus(Enum):
    UNVISITED = 1
    PROCESSING = 2
    VISITIED = 3


class Project:
    def __init__(self, project_name):
        self.project_name = project_name
        self.dependencies = 0
        self.children = []
        self.map = {}
        self.status = ProjectStatus.UNVISITED
    
    def addChild(self, new_child):
        if new_child not in self.map:
            self.children.append(new_child)
            self.map[new_child.project_name] = new_child
            new_child.incrementDependencies()
    
    def incrementDependencies(self):
        self.dependencies += 1
    
    def decrementDependencies(self):
        self.dependencies -= 1

    def getNumberOfDependencies(self):
        return self.dependencies

class Graph:
    def __init__(self):
        self.nodes = []
        self.map = {}

    def getOrCreateNode(self, node_name):
        if node_name not in self.map:
            new_node = Project(node_name)
            self.nodes.append(new_node)
            self.map[node_name] = new_node
        
        return self.map[node_name]
    
    def addEdge(self, start_node_name, end_node_name):
        start_node = self.getOrCreateNode(start_node_name)
        end_node = self.getOrCreateNode(end_node_name)

        start_node.addChild(end_node)

def breadth_first_search(ordering_project_keys, projectsGraph):
    next_to_be_processed = 0
    add_projects_with_no_deps(ordering_project_keys, projectsGraph.nodes)
    while next_to_be_processed < len(projectsGraph.nodes):
        if next_to_be_processed >= len(ordering_project_keys):
            raise RuntimeError('Cycle in the graph detected. Build order impossible')
        
        project_that_finished = projectsGraph.getOrCreateNode(ordering_project_keys[next_to_be_processed])

        for project_child in project_that_finished.children:
            project_child.decrementDependencies()
        
        add_projects_with_no_deps(ordering_project_keys, project_that_finished.children)

        next_to_be_processed += 1


def add_projects_with_no_deps(ordering_project_keys, potentiallyReadyProjects):
    for project in potentiallyReadyProjects:
        if project.getNumberOfDependencies() == 0:
            ordering_project_keys.append(project.project_name)
    

def buildDependencyGraph(projectsList, dependencies):
    graph = Graph()

    for project_name in projectsList:
        graph.getOrCreateNode(project_name)

    for dep in dependencies:
        parent_node_name, child_node_name = dep
        graph.addEdge(parent_node_name, child_node_name)
    
    return graph


def getBuildOrderBFS(projects: List[str], dependencies: List[List[str]]):
    projectsGraph = buildDependencyGraph(projects, dependencies)

    build_order_results = []

    breadth_first_search(build_order_results, projectsGraph)

    return build_order_results


def depth_first_search(projects_build_order_names, remainingProjects):
    for project in remainingProjects:
        if project.status == ProjectStatus.UNVISITED:
            project.status = ProjectStatus.PROCESSING
            depth_first_search(projects_build_order_names, project.children)
            projects_build_order_names.insert(0, project.project_name)
            project.status = ProjectStatus.VISITIED
        elif project.status == ProjectStatus.PROCESSING:
            raise RuntimeError('Cycle in the graph detected. Build order impossible')


def getBuildOrderDFS(projects: List[str], dependencies: List[List[str]]):
    projectsGraph = buildDependencyGraph(projects, dependencies)

    build_order_results = []

    depth_first_search(build_order_results, projectsGraph.nodes)

    return build_order_results


answer = getBuildOrderDFS(['A', 'B', 'C', 'D', 'E', 'F'], [
    ['A', 'D'],
    ['F', 'B'],
    ['B', 'D'],
    ['F', 'A'],
    ['D', 'C'],
])

print(answer)
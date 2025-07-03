import pygame
from abc import ABC, abstractmethod

class Behavior(ABC):
    @abstractmethod
    def calculate(self, agent, target):
        pass

class Seek(Behavior):
    def calculate(self, agent, target):
        desired = (target - agent.pos).normalize() * agent.max_speed
        steer = desired - agent.vel
        if steer.length() > agent.max_force:
            steer = steer.normalize() * agent.max_force
        return steer

class Flee(Behavior):
    def calculate(self, agent, target):
        desired = (agent.pos - target).normalize() * agent.max_speed
        steer = desired - agent.vel
        if steer.length() > agent.max_force:
            steer = steer.normalize() * agent.max_force
        return steer

class Arrival(Behavior):
    def __init__(self, raio=100):
        self.raio = raio
    def calculate(self, agent, target):
        to_target = target - agent.pos
        distancia = to_target.length()
        if distancia == 0:
            return pygame.Vector2(0, 0)
        if distancia < self.raio:
            rapidez_desejada = agent.max_speed * (distancia / self.raio)
        else:
            rapidez_desejada = agent.max_speed
        rapidez = to_target.normalize() * rapidez_desejada
        steer = rapidez - agent.vel
        if steer.length() >= agent.max_force:
            return steer.normalize() * agent.max_force
        else:
            return steer

class Wander(Behavior):
    def calculate(self, agent, target):
        desired = (target - agent.pos).normalize() * agent.max_speed
        steer = desired - agent.vel
        if steer.length() > agent.max_force:
            steer = steer.normalize() * agent.max_force
        return steer

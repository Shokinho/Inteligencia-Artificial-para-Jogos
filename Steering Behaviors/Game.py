import pygame
import random
from Agent import Agent
from Behaviors import Seek
from Behaviors import Flee
from Behaviors import Arrival
from Behaviors import Wander

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Steering Behaviors")
        self.clock = pygame.time.Clock()
        self.running = True

        
        self.imagem_do_alvo = pygame.image.load('SunflowerOUTLINED.png').convert_alpha()

        # FAZER: criar um alvo real (ex: outro agente, ou posição do mouse)
        self.target = pygame.Vector2(400, 300)

        # Cria agente com comportamento Seek
        self.seek_behavior = Seek()
        self.flee_behavior = Flee()
        self.arrival_behavior = Arrival()
        self.wander_behavior = Wander()
        self.agents = [
            Agent(pos=pygame.Vector2(200, 200), behavior=self.seek_behavior), Agent(pos=pygame.Vector2(200, 200), behavior=self.flee_behavior), Agent(pos=pygame.Vector2(200, 200), behavior=self.seek_behavior), Agent(pos=pygame.Vector2(200, 200), behavior=self.flee_behavior), Agent(pos=pygame.Vector2(200, 200), behavior=self.arrival_behavior), Agent(pos=pygame.Vector2(400, 300), behavior=self.wander_behavior), Agent(pos=pygame.Vector2(400, 300), behavior=self.wander_behavior)
        ]
        self.comportamento = "Busca"

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(60)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            # FAZER: alterar target com o mouse ou outros eventos
            #self.target = pygame.Vector2(pygame.mouse.get_pos())
            print(self.target)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_F1]:
            self.comportamento = "Busca"
            self.agents[0] = Agent(pos=pygame.Vector2(200, 200), behavior=self.seek_behavior)
        if keys[pygame.K_F2]:
            self.comportamento = "Fuga"
            self.agents[1] = Agent(pos=pygame.Vector2(200, 200), behavior=self.flee_behavior)
        if keys[pygame.K_F3]:
            self.comportamento = "Perseguir"
            self.agents[2] = Agent(pos=pygame.Vector2(200, 200), behavior=self.seek_behavior)
        if keys[pygame.K_F4]:
            self.comportamento = "Desviar"
            self.agents[3] = Agent(pos=pygame.Vector2(200, 200), behavior=self.flee_behavior)
        if keys[pygame.K_F5]:
            self.comportamento = "Chegada"
            self.agents[4] = Agent(pos=pygame.Vector2(200, 200), behavior=self.arrival_behavior)
        if keys[pygame.K_F6]:
            self.comportamento = "Vagar"
            self.agents[5] = Agent(pos=pygame.Vector2(400, 300), behavior=self.wander_behavior)
        if keys[pygame.K_F7]:
            self.comportamento = "Evitacao de obstaculos"
            self.agents[6] = Agent(pos=pygame.Vector2(400, 300), behavior=self.wander_behavior)

    def update(self):
        if self.comportamento == "Busca":
            self.target = pygame.Vector2(400, 300)
            self.agents[0].update(self.target)
        if self.comportamento == "Fuga":
            self.target = pygame.Vector2(400, 300)
            self.agents[1].update(self.target)
        if self.comportamento == "Perseguir":
            self.target = pygame.Vector2(pygame.mouse.get_pos())
            self.agents[2].update(self.target)
        if self.comportamento == "Desviar":
            self.target = pygame.Vector2(pygame.mouse.get_pos())
            self.agents[3].update(self.target)
        if self.comportamento == "Chegada":
            self.target = pygame.Vector2(400, 300)
            self.agents[4].update(self.target)
        if self.comportamento == "Vagar":
            self.target = pygame.Vector2(random.randint(0, 800), random.randint(0, 600))
            self.agents[5].update(self.target)
        if self.comportamento == "Evitacao de obstaculos":
            self.target = pygame.Vector2(random.randint(0, 800), random.randint(0, 600))
            self.agents[6].update(self.target)
        #for agent in self.agents:
        #    self.target = pygame.Vector2(random.randint(0, 800), random.randint(0, 600))
        #    agent.update(self.target)

    def draw(self):
        self.screen.fill((30, 30, 30))
        if self.comportamento == "Busca":
            # Desenha o alvo
            alvo_rect = self.imagem_do_alvo.get_rect()
            alvo_rect.center = self.target
            #pygame.draw.circle(self.screen, (255, 50, 50), self.target, 8)  # pos, raio
            self.screen.blit(self.imagem_do_alvo, alvo_rect)

            # Desenha os agentes
            self.agents[0].draw(self.screen)
        if self.comportamento == "Fuga":
            # Desenha o alvo
            alvo_rect = self.imagem_do_alvo.get_rect()
            alvo_rect.center = self.target
            #pygame.draw.circle(self.screen, (255, 50, 50), self.target, 8)  # pos, raio
            self.screen.blit(self.imagem_do_alvo, alvo_rect)

            # Desenha os agentes
            self.agents[1].draw(self.screen)
        if self.comportamento == "Perseguir":
            # Desenha o alvo
            alvo_rect = self.imagem_do_alvo.get_rect()
            alvo_rect.center = self.target
            #pygame.draw.circle(self.screen, (255, 50, 50), self.target, 8)  # pos, raio
            self.screen.blit(self.imagem_do_alvo, alvo_rect)

            # Desenha os agentes
            self.agents[2].draw(self.screen)
        if self.comportamento == "Desviar":
            # Desenha o alvo
            alvo_rect = self.imagem_do_alvo.get_rect()
            alvo_rect.center = self.target
            #pygame.draw.circle(self.screen, (255, 50, 50), self.target, 8)  # pos, raio
            self.screen.blit(self.imagem_do_alvo, alvo_rect)

            # Desenha os agentes
            self.agents[3].draw(self.screen)
        if self.comportamento == "Chegada":
            # Desenha o alvo
            alvo_rect = self.imagem_do_alvo.get_rect()
            alvo_rect.center = self.target
            #pygame.draw.circle(self.screen, (255, 50, 50), self.target, 8)  # pos, raio
            self.screen.blit(self.imagem_do_alvo, alvo_rect)

            # Desenha os agentes
            self.agents[4].draw(self.screen)
        if self.comportamento == "Vagar":
            # Desenha os agentes
            self.agents[5].draw(self.screen)
        if self.comportamento == "Evitacao de obstaculos":
            # Desenha os agentes
            self.agents[6].draw(self.screen)
        # Desenha o alvo
        #alvo_rect = self.imagem_do_alvo.get_rect()
        #alvo_rect.center = self.target
        #pygame.draw.circle(self.screen, (255, 50, 50), self.target, 8)  # pos, raio
        #self.screen.blit(self.imagem_do_alvo, alvo_rect)

        # Desenha os agentes
        #for agent in self.agents:
        #    agent.draw(self.screen)

        pygame.display.flip()


if __name__ == "__main__":
    game = Game()
    game.run()
    pygame.quit()

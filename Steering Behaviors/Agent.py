import pygame

class Agent:
    def __init__(self, pos, behavior):
        self.pos = pos
        self.vel = pygame.Vector2(0, 0)
        self.max_speed = 2.5
        self.max_force = 0.05
        self.behavior = behavior
        self.imagem_do_agente = pygame.image.load('abelha.png').convert_alpha()

        # Representação visual: triângulo
        self.size = 20

    def update(self, target):
        steering = self.behavior.calculate(self, target)
        self.vel += steering
        self.vel = self.vel.normalize() * self.max_speed if self.vel.length() > self.max_speed else self.vel
        self.pos += self.vel

    def draw(self, surface):
        # Desenha um triângulo apontando na direção da velocidade
        agente_rect = self.imagem_do_agente.get_rect()
        agente_rect.center = self.pos
        angle = self.vel.angle_to(pygame.Vector2(1, 0))
        #agente_rect = pygame.transform.rotate(self.imagem_do_agente, angle)
        #self.imagem_do_agente = pygame.transform.rotate(surface, angle)
        surface.blit(self.imagem_do_agente, agente_rect)
        
        points = [
            (self.pos + pygame.Vector2(self.size, 0).rotate(-angle)),
            (self.pos + pygame.Vector2(-self.size / 2, self.size / 2).rotate(-angle)),
            (self.pos + pygame.Vector2(-self.size / 2, -self.size / 2).rotate(-angle)),
        ]
        #pygame.draw.polygon(surface, (255, 100, 100), points)

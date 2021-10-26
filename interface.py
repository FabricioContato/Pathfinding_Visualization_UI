from Matrix import Matrix
from searchs import *
import pygame

pygame.init()

RIGHT_CLICK = 2
LEFT_CLICK = 0

STATE_CHOOSE_THE_END_CELL = 0
STATE_CHOOSE_THE_START_CELL = 1
STATE_CHOOSE_UNACCESSIBLE_CELS = 2
STATE_CHOOSE_THE_SHEARC = 3
STATE_RUN_THE_SEARCH = 4
WHAT_NEXT = 5

class Interface:
    def __init__(self, screen_dimension,graph_width,graph_heigt):
        self.screen = pygame.display.set_mode(screen_dimension)
        self.matrix = Matrix(screen_dimension,graph_heigt,graph_width)
        self.clock = clock = pygame.time.Clock()

        self.state = STATE_CHOOSE_THE_END_CELL
        self.search = None
        self.serach_dic = getSerach_dic()
        self.print_axu = True
        self.pressed_number = None




    def updateScreen(self):
        self.screen.blit(self.matrix.getSprite(),(0,0))
        pygame.display.flip()

    def enter_key_pess(self):
        return pygame.key.get_pressed()[pygame.K_KP_ENTER]

    def f1_key_pess(self):
        return pygame.key.get_pressed()[pygame.K_F1]

    def f2_key_press(self):
        return pygame.key.get_pressed()[pygame.K_F2]

    def f3_key_press(self):
        return pygame.key.get_pressed()[pygame.K_F3]

    def _0_key_press(self):
        return pygame.key.get_pressed()[pygame.K_0]

    def _1_key_press(self):
        return pygame.key.get_pressed()[pygame.K_1]

    def _2_key_press(self):
        return pygame.key.get_pressed()[pygame.K_2]

    def _3_key_press(self):
        return pygame.key.get_pressed()[pygame.K_3]

    def _4_key_press(self):
        return pygame.key.get_pressed()[pygame.K_4]

    def _5_key_press(self):
        return pygame.key.get_pressed()[pygame.K_5]

    def _6_key_press(self):
        return pygame.key.get_pressed()[pygame.K_6]

    def _7_key_press(self):
        return pygame.key.get_pressed()[pygame.K_7]

    def _8_key_press(self):
        return pygame.key.get_pressed()[pygame.K_8]

    def _9_key_press(self):
        return pygame.key.get_pressed()[pygame.K_9]

    def number_key_press(self):
        self.pressed_number = None

        if self._0_key_press():
            self.pressed_number = 0
        elif self._1_key_press():
            self.pressed_number = 1
        elif self._2_key_press():
            self.pressed_number = 2
        elif self._3_key_press():
            self.pressed_number = 3
        elif self._4_key_press():
            self.pressed_number = 4
        elif self._5_key_press():
            self.pressed_number = 5
        elif self._6_key_press():
            self.pressed_number = 6
        elif self._7_key_press():
            self.pressed_number = 7
        elif self._8_key_press():
            self.pressed_number = 8
        elif self._9_key_press():
            self.pressed_number = 9

        if self.pressed_number != None:
            return True
        return False

    def right_mouse_click(self, event):
        return pygame.mouse.get_pressed()[RIGHT_CLICK] and event.type == pygame.MOUSEBUTTONDOWN

    def left_mouse_click(self, event):
        return pygame.mouse.get_pressed()[LEFT_CLICK] and event.type == pygame.MOUSEBUTTONDOWN

    def choose_the_end_cell(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.matrix.cell_click_check_for_end()
            self.state = STATE_CHOOSE_THE_START_CELL

    def choose_the_start_cell(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.matrix.cell_click_check_for_start()
            self.state = STATE_CHOOSE_UNACCESSIBLE_CELS

    def choose_unaccessible_accessible_cells(self, event):
        if self.left_mouse_click(event):
            self.matrix.cell_click_check_for_unaccessible_or_acessible()

        elif self.right_mouse_click(event):
            self.matrix.line_draw()

        elif self.f1_key_pess():
            self.matrix.random_unaccessible_cells()

        elif self.number_key_press():
            self.matrix.set_cost(self.pressed_number)

        elif self.enter_key_pess():
            self.state = STATE_CHOOSE_THE_SHEARC


    def choose_the_search(self):
        if self.print_axu :
            print("Serch options:")
            for key, value in search_dic.items():
                print(f" {key} : {value[1]}")
            self.print_axu = False

        if self.number_key_press():
            self.search = search_dic[self.pressed_number][0]
            self.state = STATE_RUN_THE_SEARCH
            self.print_axu = True


    def path_track(self,node):
        if node != None:
            while(node.getParent() != None):
                node.setAsPath()
                node = node.getParent()
                #self.matrix.blitCell(node.getCell())

    def what_next(self):
        if self.print_axu:
            print("options \n f2 - re-start process \n f3 - exit")
            self.print_axu = False
        if self.f2_key_press():
            self.matrix.reset()
            self.state = STATE_CHOOSE_THE_END_CELL
            self.print_axu = True
            self.pressed_number = None
        elif self.f3_key_press():
            pygame.quit()


    def gameLoop(self):
        while(True):
            for event in pygame.event.get():
                if self.state == STATE_CHOOSE_THE_END_CELL:
                    self.choose_the_end_cell(event)
                elif self.state == STATE_CHOOSE_THE_START_CELL:
                    self.choose_the_start_cell(event)
                elif self.state == STATE_CHOOSE_UNACCESSIBLE_CELS:
                    self.choose_unaccessible_accessible_cells(event)
                elif self.state == STATE_CHOOSE_THE_SHEARC:
                    self.choose_the_search()
                elif self.state == STATE_RUN_THE_SEARCH:
                    node = self.search(self.matrix,self)
                    self.path_track(node)
                    self.state = WHAT_NEXT
                elif self.state == WHAT_NEXT:
                    self.what_next()



            self.updateScreen()

def interface_factory():
    print(" screen dimension \n 1 - 800x600 \n 2 - 1200x700 ")
    choice = int(input())
    if choice == 1:
        sd = (800,600)
    elif choice == 2:
        sd = (1200,700)

    print(" graph dimension \n 1 - 10x10 \n 2 - 20x20 \n 3 - 50x50 \n 4 - 60x60 \n 5 - 100x100 \n 6 - 200x200")
    choice = int(input())
    if choice == 1:
        gw = 10
        gh = 10
    elif choice == 2:
        gw = 20
        gh = 20
    elif choice == 3:
        gw = 50
        gh = 50
    elif choice == 4:
        gw = 60
        gh = 60
    elif choice == 5:
        gw = 100
        gh = 100
    elif choice == 6:
        gw = 200
        gh = 200

    return Interface(sd,gw,gh)





interface = interface_factory()
interface.gameLoop()

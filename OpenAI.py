
def main():
    # get a 3d image of the name "Mathilda" in red
    mathilda_3d = get_3d_mathilda()

    # create a 3d image of the name "Mathilda" in red
    mathilda_3d_image = create_3d_image(mathilda_3d)

    # display the 3d image of the name "Mathilda" in red
    display_3d_image(mathilda_3d_image)


def get_3d_mathilda():
    # create an empty 3d image
    mathilda_3d = []

    # open the image file
    image_file = open('mathilda.txt', 'r')

    # read the image file
    for line in image_file:
        # convert the line to an integer list
        line_list = [int(number) for number in line.split()]

        # add the line list to the 3d image
        mathilda_3d.append(line_list)

    # close the image file
    image_file.close()

    # return the 3d image
    return mathilda_3d


def create_3d_image(mathilda_3d):
    # create an empty 3d image
    mathilda_3d_image = []

    # for each row in the 3d image
    for row in range(len(mathilda_3d)):
        # create an empty row
        mathilda_3d_image_row = []

        # for each column in the 3d image
        for column in range(len(mathilda_3d[row])):
            # if the pixel is not 0
            if mathilda_3d[row][column] != 0:
                # create a red pixel
                pixel = (255, 0, 0)
            else:
                # create a black pixel
                pixel = (0, 0, 0)

            # add the pixel to the row
            mathilda_3d_image_row.append(pixel)

        # add the row to the 3d image
        mathilda_3d_image.append(mathilda_3d_image_row)

    # return the 3d image
    return mathilda_3d_image


def display_3d_image(mathilda_3d_image):
    # create a display surface
    display_surface = pygame.display.set_mode((len(mathilda_3d_image[0]), len(mathilda_3d_image)))

    # set the title of the display surface
    pygame.display.set_caption('Mathilda')

    # create a game surface
    game_surface = pygame.Surface(display_surface.get_size())
    game_surface = game_surface.convert()

    # for each row in the 3d image
    for row in range(len(mathilda_3d_image)):
        # for each column in the 3d image
        for column in range(len(mathilda_3d_image[row])):
            # draw the pixel
            pygame.draw.rect(game_surface, mathilda_3d_image[row][column], (column, row, 1, 1))

    # while the user hasn't quit
    while not has_quit():
        # fill the display surface with a black background
        display_surface.fill((0, 0, 0))

        # draw the game surface on the display surface
        display_surface.blit(game_surface, (0, 0))

        # update the display
        pygame.display.flip()


def has_quit():
    # for each event
    for event in pygame.event.get():
        # if the event is the quit event
        if event.type == pygame.QUIT:
            # return True
            return True

    # return False
    return False


# run the main function
main()
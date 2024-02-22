from manim import *

class DoubleLineChartScene(Scene):
    def construct(self):
        # Define the axes
        axes = Axes(
            x_range=[0, 5, 1],
            y_range=[-6, 4, 1],
            x_length=6,
            y_length=6,
            axis_config={"color": BLUE},
        )

        # Points for the first line chart
        points1 = [[0, 1], [2, 3], [4, -5]]
        # Points for the second line chart
        points2 = [[0, 0], [1, 1], [0, 0]]

        # Plot the first line graph
        graph1 = axes.plot_line_graph(
            x_values=[p[0] for p in points1],
            y_values=[p[1] for p in points1],
            line_color=RED,
            vertex_dot_style=dict(stroke_width=3, fill_color=YELLOW),
            stroke_width=4,
        )

        # Plot the second line graph
        graph2 = axes.plot_line_graph(
            x_values=[p[0] for p in points2],
            y_values=[p[1] for p in points2],
            line_color=GREEN,
            vertex_dot_style=dict(stroke_width=3, fill_color=ORANGE),
            stroke_width=4,
        )

        # Extract the plotted lines from the graphs
        line_graph1 = graph1["line_graph"]
        line_graph2 = graph2["line_graph"]
        
        # Create dots that will move along the lines
        moving_dot1 = Dot(color=YELLOW, radius=0.1).move_to(axes.c2p(*points1[0]))
        moving_dot2 = Dot(color=ORANGE, radius=0.1).move_to(axes.c2p(*points2[0]))

        # Create the animations of the dots moving along the lines
        dot_animation1 = MoveAlongPath(moving_dot1, line_graph1)
        dot_animation2 = MoveAlongPath(moving_dot2, line_graph2)

        # Add axes and lines to the scene
        self.add(axes, line_graph1, moving_dot1, line_graph2, moving_dot2)
        # Play the animations of the dots moving simultaneously
        self.play(dot_animation1, dot_animation2)


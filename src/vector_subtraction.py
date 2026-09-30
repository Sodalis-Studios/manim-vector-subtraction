from manim import *

# =============================================================================
# CONSTANTS
# =============================================================================

# Colors
A_COLOR = YELLOW
B_COLOR = BLUE
R_COLOR = PURPLE_B
OPPOSITE_R_COLOR = MAROON
X_COLOR = RED
Y_COLOR = GREEN

# Vector components
A_X, A_Y = 1, 3
B_X, B_Y = 4, 2
R_X = B_X - A_X
R_Y = B_Y - A_Y

# Layout
LABEL_FONT_SIZE = 32
VECTOR_LABEL_OFFSET = LEFT * 0.2 + DOWN * 0.35


def apply_component_colors(*equations):
    """Color vectors (A, B, R) and their x / y subscripts inside the given equations."""
    for equation in equations:
        equation.set_color_by_tex("A", A_COLOR)
        equation.set_color_by_tex("B", B_COLOR)
        equation.set_color_by_tex("R", R_COLOR)
        equation.set_color_by_tex("_x", X_COLOR)
        equation.set_color_by_tex("_y", Y_COLOR)


class VectorSubtraction(MovingCameraScene):
    """Explains the vector subtraction B - A, first numerically and then geometrically."""

    def construct(self):
        self._show_numerical_section()
        self._show_visual_section()
        self._show_polar_form()
        self._show_algebraic_rewrite()
        self._show_geometric_addition()
        self._show_path_a_then_b()
        self._show_path_b_then_a()
        self._show_conclusions()

    # =========================================================================
    # NUMERICAL SECTION
    # =========================================================================
    def _show_numerical_section(self):
        self.next_section("Numerical Section")

        # Symbolic definitions: A = (A_x, A_y) and B = (B_x, B_y)
        eq_a_symbolic = MathTex(r"\vec{A}", "=", "(", "A", "_x", ",", "A", "_y", ")")
        eq_b_symbolic = MathTex(r"\vec{B}", "=", "(", "B", "_x", ",", "B", "_y", ")")

        eq_a_symbolic.set_color(A_COLOR)
        eq_b_symbolic.set_color(B_COLOR)
        apply_component_colors(eq_a_symbolic, eq_b_symbolic)

        VGroup(eq_a_symbolic, eq_b_symbolic).arrange(DOWN, aligned_edge=LEFT).shift(
            UP * 1.5
        )

        self.play(
            Write(eq_a_symbolic[0]),
            Write(eq_b_symbolic[0]),
            run_time=2.0,
            rate_func=smooth,
        )
        self.wait(2.0)
        self.play(
            Write(eq_a_symbolic[1:]),
            Write(eq_b_symbolic[1:]),
            run_time=2.0,
            rate_func=smooth,
        )
        self.wait(2.0)

        # Numeric definitions: A = (1_x, 3_y) and B = (4_x, 2_y)
        eq_a_numeric = MathTex(
            r"\vec{A}", "=", "(", str(A_X), "_x", ",", str(A_Y), "_y", ")"
        )
        eq_b_numeric = MathTex(
            r"\vec{B}", "=", "(", str(B_X), "_x", ",", str(B_Y), "_y", ")"
        )

        eq_a_numeric.move_to(eq_a_symbolic, aligned_edge=LEFT)
        eq_b_numeric.move_to(eq_b_symbolic, aligned_edge=LEFT)

        eq_a_numeric.set_color(A_COLOR)
        eq_b_numeric.set_color(B_COLOR)
        apply_component_colors(eq_a_numeric, eq_b_numeric)

        self.play(
            ReplacementTransform(eq_a_symbolic, eq_a_numeric),
            ReplacementTransform(eq_b_symbolic, eq_b_numeric),
            run_time=2.0,
        )
        self.wait(1.5)

        # Subtraction: B - A = (B_x - A_x, B_y - A_y)
        #
        # Submobject indices of eq_subtraction:
        #    0: \vec{B}    1: -    2: \vec{A}    3: =    4: (
        #    5: B_x value  6: _x   7: -    8: A_x value  9: _x   10: ,
        #   11: B_y value 12: _y  13: -   14: A_y value 15: _y   16: )
        eq_subtraction = MathTex(
            r"\vec{B}",
            "-",
            r"\vec{A}",
            "=",
            "(",
            str(B_X),
            "_x",
            "-",
            str(A_X),
            "_x",
            ",",
            str(B_Y),
            "_y",
            "-",
            str(A_Y),
            "_y",
            ")",
        )
        apply_component_colors(eq_subtraction)
        eq_subtraction[5].set_color(B_COLOR)  # B_x value
        eq_subtraction[8].set_color(A_COLOR)  # A_x value
        eq_subtraction[11].set_color(B_COLOR)  # B_y value
        eq_subtraction[14].set_color(A_COLOR)  # A_y value
        eq_subtraction.shift(DOWN * 1)

        # Fixed parts of the equation (everything except the numbers and their subscripts)
        subtraction_template = VGroup(
            eq_subtraction[0],
            eq_subtraction[1],
            eq_subtraction[2],
            eq_subtraction[3],
            eq_subtraction[4],  # \vec{B} - \vec{A} = (
            eq_subtraction[7],  # -
            eq_subtraction[10],  # ,
            eq_subtraction[13],  # -
            eq_subtraction[16],  # )
        )
        subtraction_template[0].set_color(B_COLOR)
        subtraction_template[2].set_color(A_COLOR)
        self.play(Write(subtraction_template), run_time=2.0)
        self.wait(1.0)

        # Move the numbers into the subtraction: x components first, then y components
        self.play(
            ReplacementTransform(
                eq_b_numeric[3].copy(), eq_subtraction[5]
            ),  # B_x value
            ReplacementTransform(
                eq_b_numeric[4].copy(), eq_subtraction[6]
            ),  # _x subscript
            ReplacementTransform(
                eq_a_numeric[3].copy(), eq_subtraction[8]
            ),  # A_x value
            ReplacementTransform(
                eq_a_numeric[4].copy(), eq_subtraction[9]
            ),  # _x subscript
            run_time=2.0,
        )
        self.play(
            ReplacementTransform(
                eq_b_numeric[6].copy(), eq_subtraction[11]
            ),  # B_y value
            ReplacementTransform(
                eq_b_numeric[7].copy(), eq_subtraction[12]
            ),  # _y subscript
            ReplacementTransform(
                eq_a_numeric[6].copy(), eq_subtraction[14]
            ),  # A_y value
            ReplacementTransform(
                eq_a_numeric[7].copy(), eq_subtraction[15]
            ),  # _y subscript
            run_time=2.0,
        )
        self.wait(2.0)

        # Result: R = (3_x, -1_y)
        eq_result = MathTex(
            r"\vec{R}", "=", "(", str(R_X), "_x", ",", str(R_Y), "_y", ")"
        )
        eq_result.next_to(eq_subtraction, ORIGIN)

        eq_result.set_color(R_COLOR)
        apply_component_colors(eq_result)

        self.play(Transform(eq_subtraction, eq_result), run_time=2.0)
        self.wait(2.0)

        # Clear the scene
        self.play(FadeOut(*self.mobjects))
        self.wait(2.0)

    # =========================================================================
    # VISUAL SECTION: PLANE, VECTORS A, B AND R
    # =========================================================================
    def _show_visual_section(self):
        self.next_section("Visual Section")

        # Coordinate plane
        self.plane = NumberPlane(
            x_axis_config={"color": RED},
            y_axis_config={"color": GREEN},
            x_range=[-3, 7, 1],
            y_range=[-5, 6, 1],
            axis_config={"include_numbers": True, "include_tip": True},
            background_line_style={
                "stroke_color": WHITE,
                "stroke_width": 1,
                "stroke_opacity": 0.3,
            },
        )
        plane = self.plane

        self.camera.frame.move_to(plane.c2p(2, 2))

        self.play(Create(plane), run_time=4.0, rate_func=linear)
        self.wait(1.0)

        self.plane_origin = plane.c2p(0, 0)

        # Vectors
        self.vector_a = Arrow(
            start=self.plane_origin, end=plane.c2p(A_X, A_Y), color=A_COLOR, buff=0
        )
        self.vector_b = Arrow(
            start=self.plane_origin, end=plane.c2p(B_X, B_Y), color=B_COLOR, buff=0
        )
        # R drawn from the origin
        self.vector_r = Arrow(
            start=self.plane_origin, end=plane.c2p(R_X, R_Y), color=R_COLOR, buff=0
        )
        # R drawn from the tip of A to the tip of B (the actual subtraction B - A)
        vector_r_tip_to_tip = Arrow(
            start=self.vector_a.get_end(),
            end=self.vector_b.get_end(),
            color=R_COLOR,
            buff=0,
        )

        # Labels
        self.label_a = MathTex(
            r"\vec{A}",
            "=",
            "(",
            str(A_X),
            "_x",
            ",",
            str(A_Y),
            "_y",
            ")",
            color=A_COLOR,
            font_size=LABEL_FONT_SIZE,
        ).next_to(self.vector_a.get_end(), UP)
        self.label_b = MathTex(
            r"\vec{B}",
            "=",
            "(",
            str(B_X),
            "_x",
            ",",
            str(B_Y),
            "_y",
            ")",
            color=B_COLOR,
            font_size=LABEL_FONT_SIZE,
        ).next_to(self.vector_b.get_end(), RIGHT)
        label_r_with_components = MathTex(
            r"\vec{R}",
            "=",
            "(",
            str(R_X),
            "_x",
            ",",
            str(R_Y),
            "_y",
            ")",
            color=R_COLOR,
            font_size=LABEL_FONT_SIZE,
        ).next_to(self.vector_r.get_end(), RIGHT)
        self.label_r = MathTex(
            r"\vec{R}", color=R_COLOR, font_size=LABEL_FONT_SIZE
        ).next_to(vector_r_tip_to_tip.get_center(), UP)
        apply_component_colors(
            self.label_a, self.label_b, label_r_with_components, self.label_r
        )

        self.play(GrowArrow(self.vector_a), Write(self.label_a), run_time=2.0)
        self.play(GrowArrow(self.vector_b), Write(self.label_b), run_time=2.0)
        self.play(
            GrowArrow(self.vector_r), Write(label_r_with_components), run_time=2.0
        )
        self.wait(1.0)

        # Slide R from the origin to the tip of A
        self.play(Transform(self.vector_r, vector_r_tip_to_tip), run_time=1.0)
        self.play(
            ReplacementTransform(label_r_with_components, self.label_r), run_time=1.0
        )
        self.wait(1.0)

    # =========================================================================
    # POLAR FORM OF THE RESULT VECTOR
    # =========================================================================
    def _show_polar_form(self):
        vector_r = self.vector_r
        label_r = self.label_r

        # Save the current state of R so it can be restored later
        vector_r.save_state()
        label_r.save_state()
        self.background_group = VGroup(
            self.plane, self.vector_a, self.vector_b, self.label_a, self.label_b
        )

        self.play(FadeOut(self.background_group), run_time=2.0)

        # Move R to the center of the screen
        monitor_center = self.camera.frame.get_center()

        self.play(
            vector_r.animate.move_to(monitor_center),
            label_r.animate.move_to(monitor_center + VECTOR_LABEL_OFFSET),
            run_time=1.5,
        )
        self.wait(2.0)

        # Geometry: angle and magnitude
        reference_line = DashedLine(
            vector_r.get_start(), vector_r.get_start() + RIGHT * 4, color=GRAY
        )

        angle = Angle(vector_r, reference_line, radius=1.5, color=ORANGE)
        angle_label = MathTex(r"\theta", font_size=36, color=ORANGE).next_to(
            angle, RIGHT, buff=0.2
        )

        magnitude_label = MathTex(r"||\vec{R}||", color=PURPLE, font_size=36).move_to(
            label_r.get_center()
        )

        self.play(
            Create(reference_line), Create(angle), Write(angle_label), run_time=2.0
        )
        self.play(Transform(label_r, magnitude_label), run_time=2.0)
        self.wait(2.0)

        # Stretch & squash effect: the angle and labels follow the vector
        angle.add_updater(
            lambda m: m.become(
                Angle(vector_r, reference_line, radius=1.5, color=ORANGE)
            )
        )
        angle_label.add_updater(lambda m: m.next_to(angle, RIGHT, buff=0.2))
        label_r.add_updater(
            lambda m: m.move_to(vector_r.get_center() + VECTOR_LABEL_OFFSET)
        )

        # Rotate the vector and bring it back (changes the angle)
        self.play(
            Rotate(vector_r, angle=-0.8, about_point=vector_r.get_start()),
            rate_func=there_and_back,
            run_time=2.0,
        )
        self.wait(1.0)

        # Scale the vector up and bring it back (changes the magnitude)
        self.play(
            vector_r.animate.scale(1.6, about_point=vector_r.get_start()),
            rate_func=there_and_back,
            run_time=2.0,
        )

        # Remove the updaters so they don't interfere with later animations
        angle.clear_updaters()
        angle_label.clear_updaters()
        label_r.clear_updaters()
        self.wait(2.0)

        polar_form_text = MathTex(
            r"\text{Forma Polar: } \|\vec{R}\| \angle \theta", font_size=36
        )
        polar_form_text.next_to(self.camera.frame.get_top(), DOWN, buff=0.5)

        self.play(Write(polar_form_text), run_time=2.0)
        self.wait(1.5)

        # Free copies of R placed around the screen (same magnitude and angle)
        vector_copies, copy_labels = self._create_free_vector_copies()

        self.play(
            LaggedStart(*[Create(v) for v in vector_copies], lag_ratio=0.9),
            run_time=5.0,
            rate_func=linear,
        )
        self.wait(1.0)

        self.play(Write(copy_labels), run_time=1.5)
        self.wait(2.0)

        # Remove the temporary geometry
        self.play(
            FadeOut(reference_line),
            FadeOut(angle),
            FadeOut(angle_label),
            FadeOut(vector_copies),
            FadeOut(copy_labels),
            FadeOut(polar_form_text),
        )

        # Restore R to its original position and bring back the background
        self.play(
            Restore(vector_r),
            Restore(label_r),
            FadeIn(self.background_group),
            run_time=1.5,
        )

    def _create_free_vector_copies(self):
        """Return copies of vector R shifted to different places, along with their labels."""
        offsets = [
            UP * 2 + RIGHT * 4,
            DOWN * 2 + RIGHT * 4,
            LEFT * 5,
            DOWN * 2 + LEFT * 4,
            UP * 2.7 + LEFT * 3.3,
        ]

        vector_copies = VGroup()
        copy_labels = VGroup()

        for offset in offsets:
            vector_copy = self.vector_r.copy()
            vector_copy.shift(offset)  # A free vector floating in space
            vector_copies.add(vector_copy)

            copy_label = MathTex(r"\vec{R}", color=R_COLOR, font_size=LABEL_FONT_SIZE)
            copy_label.move_to(vector_copy.get_center() + VECTOR_LABEL_OFFSET)
            copy_labels.add(copy_label)

        return vector_copies, copy_labels

    # =========================================================================
    # ALGEBRAIC REWRITE: B - A  ->  (-A) + B
    # =========================================================================
    def _show_algebraic_rewrite(self):
        self.play(
            FadeOut(self.background_group, self.vector_r, self.label_r),
        )

        camera_center = self.camera.frame.get_center()

        eq_subtract = MathTex(r"\vec{B}", r"-\vec{A}", font_size=72).move_to(
            camera_center
        )
        eq_subtract[0].set_color(B_COLOR)
        eq_subtract[1].set_color(A_COLOR)

        self.play(Write(eq_subtract), run_time=2.0)
        self.wait(1.0)

        eq_opposite_addition = MathTex(
            "(", r"-\vec{A}", ")", "+", r"\vec{B}", font_size=72
        ).move_to(camera_center)
        eq_opposite_addition[:3].set_color(A_COLOR)
        eq_opposite_addition[4].set_color(B_COLOR)

        self.play(TransformMatchingTex(eq_subtract, eq_opposite_addition), run_time=2.0)
        self.wait(2.0)

        self.play(FadeOut(eq_opposite_addition))

        # Bring back the geometric scene
        self.play(FadeIn(self.background_group, self.vector_r, self.label_r))
        self.wait(1.0)

    # =========================================================================
    # GEOMETRIC ADDITION: (-A) + B = R
    # =========================================================================
    def _show_geometric_addition(self):
        plane = self.plane
        vector_a, label_a = self.vector_a, self.label_a
        vector_b, label_b = self.vector_b, self.label_b
        vector_r, label_r = self.vector_r, self.label_r

        # Zoom out and move the camera down
        self.camera.frame.save_state()
        self.play(self.camera.frame.animate.scale(1.3).shift(DOWN * 0.8), run_time=2.0)

        vector_a.save_state()
        label_a.save_state()
        vector_b.save_state()
        label_b.save_state()
        vector_r.save_state()
        label_r.save_state()

        # A becomes -A
        vector_opposite_a = Arrow(
            start=self.plane_origin, end=plane.c2p(-A_X, -A_Y), color=A_COLOR, buff=0
        )
        label_opposite_a = MathTex(
            r"-\vec{A}",
            "=",
            "(",
            str(-A_X),
            "_x",
            ",",
            str(-A_Y),
            "_y",
            ")",
            color=A_COLOR,
            font_size=LABEL_FONT_SIZE,
        ).next_to(vector_opposite_a.get_end(), LEFT * 0.5)
        apply_component_colors(label_opposite_a)

        self.play(
            Transform(vector_a, vector_opposite_a),
            Transform(label_a, label_opposite_a),
            run_time=2.0,
        )
        self.wait(1.0)

        # B is placed at the tip of -A
        vector_b_from_opposite_a = Arrow(
            start=vector_a.get_end(), end=plane.c2p(R_X, R_Y), color=B_COLOR, buff=0
        )

        label_b_only = MathTex(r"\vec{B}", color=B_COLOR, font_size=LABEL_FONT_SIZE)
        label_b_only.next_to(
            vector_b_from_opposite_a.get_center(), RIGHT + DOWN * 0.2, buff=0.1
        )

        self.play(
            Transform(vector_b, vector_b_from_opposite_a),
            Transform(label_b, label_b_only),
            run_time=2.0,
        )

        # B ends exactly at the tip of R, showing that (-A) + B = R
        self.wait(1.0)

        shift_to_origin = self.plane_origin - vector_r.get_start()
        self.play(
            vector_r.animate.shift(shift_to_origin),
            label_r.animate.shift(shift_to_origin),
            run_time=2.0,
        )

        # Highlight the tip where both paths meet
        self.play(Flash(vector_r.get_end(), color=PURPLE, line_length=0.2))
        self.wait(1.0)

        self.play(FadeOut(vector_r), FadeOut(label_r))

        self.play(
            Restore(self.camera.frame),
            Restore(vector_a),
            Restore(label_a),
            Restore(vector_b),
            Restore(label_b),
            run_time=2.0,
        )

    # =========================================================================
    # PATH EXPLANATION: A -> origin -> B
    # =========================================================================
    def _show_path_a_then_b(self):
        vector_r, label_r = self.vector_r, self.label_r

        self._animate_dot_path(
            start_vector=self.vector_a,
            end_vector=self.vector_b,
            glow_colors=(PURPLE_B, PURPLE_D),
            first_trail_color=PURPLE_D,
            second_trail_color=PURPLE_B,
            flash_color=PURPLE,
        )

        # Bring back R and show it as (-A) + B
        vector_r.restore()
        label_r.restore()
        label_opposite_a_plus_b = MathTex(
            r"(-\vec{A}) + \vec{B}", color=R_COLOR, font_size=LABEL_FONT_SIZE
        ).next_to(label_r.get_center(), ORIGIN + RIGHT * 0.1)
        apply_component_colors(label_opposite_a_plus_b)
        self.play(GrowArrow(vector_r), Write(label_r), run_time=2.0)
        self.wait(1.0)
        self.play(Transform(label_r, label_opposite_a_plus_b), run_time=2.0)

        self.wait(1.0)
        self.play(FadeOut(vector_r), FadeOut(label_r))
        self.wait(0.5)

    # =========================================================================
    # PATH EXPLANATION (REVERSED): B -> origin -> A
    # =========================================================================
    def _show_path_b_then_a(self):
        vector_a, vector_b = self.vector_a, self.vector_b

        self._animate_dot_path(
            start_vector=vector_b,
            end_vector=vector_a,
            glow_colors=(MAROON_B, MAROON_D),
            first_trail_color=MAROON_D,
            second_trail_color=MAROON_B,
            flash_color=OPPOSITE_R_COLOR,
        )

        # The opposite vector -R goes from the tip of B to the tip of A
        vector_opposite_r = Arrow(
            start=vector_b.get_end(),
            end=vector_a.get_end(),
            color=OPPOSITE_R_COLOR,
            buff=0,
        )
        label_opposite_r = MathTex(
            r"-\vec{R}", color=OPPOSITE_R_COLOR, font_size=LABEL_FONT_SIZE
        ).next_to(vector_opposite_r.get_center(), UP)
        label_opposite_b_plus_a = MathTex(
            r"(-\vec{B}) + \vec{A}", color=OPPOSITE_R_COLOR, font_size=LABEL_FONT_SIZE
        ).next_to(label_opposite_r.get_center(), ORIGIN + RIGHT * 0.1)
        apply_component_colors(label_opposite_r, label_opposite_b_plus_a)

        self.play(GrowArrow(vector_opposite_r), Write(label_opposite_r), run_time=2.0)
        self.wait(1.0)

        self.play(Transform(label_opposite_r, label_opposite_b_plus_a), run_time=1.0)
        self.wait(2.0)

        self.play(FadeOut(*self.mobjects))

    def _create_glowing_dot(self, position, glow_colors):
        """Create a white dot with two translucent halos to simulate a glow.

        glow_colors is a tuple (inner_halo_color, outer_halo_color).
        """
        inner_color, outer_color = glow_colors
        core = Dot(position, color=WHITE, radius=0.1)
        inner_glow = Dot(position, color=inner_color, radius=0.24, fill_opacity=0.4)
        outer_glow = Dot(position, color=outer_color, radius=0.40, fill_opacity=0.1)
        return VGroup(outer_glow, inner_glow, core)

    def _animate_dot_path(
        self,
        start_vector,
        end_vector,
        glow_colors,
        first_trail_color,
        second_trail_color,
        flash_color,
    ):
        """Move a glowing dot from the tip of start_vector to the origin (undoing it),
        then to the tip of end_vector (adding it), leaving a trail behind."""
        dot = self._create_glowing_dot(start_vector.get_end(), glow_colors)

        # TracedPath follows the center of the dot group while it moves
        first_trail = TracedPath(
            dot.get_center, stroke_color=first_trail_color, stroke_width=3
        )

        self.play(FadeIn(dot))
        self.add(first_trail)
        self.wait(1.0)

        # Trip 1: undo the start vector (from its tip to the origin)
        self.play(dot.animate.move_to(self.plane_origin), run_time=2.0)
        self.wait(0.5)

        # Trip 2: add the end vector (from the origin to its tip), with a new trail
        second_trail = TracedPath(
            dot.get_center, stroke_color=second_trail_color, stroke_width=3
        )
        self.add(second_trail)

        self.play(dot.animate.move_to(end_vector.get_end()), run_time=2.0)
        self.wait(0.5)

        # Highlight the arrival point
        self.play(Flash(dot, color=flash_color, line_length=0.4))
        self.wait(0.5)

        # Remove the dot and its trails
        self.play(FadeOut(dot), FadeOut(first_trail), FadeOut(second_trail))
        self.wait(0.5)

    # =========================================================================
    # CONCLUSIONS
    # =========================================================================
    def _show_conclusions(self):
        # Exact camera center after all the camera movements
        final_camera_center = self.camera.frame.get_center()

        # Title, moved to the top edge of the camera frame
        title = MathTex(r"\text{Conclusiones}", font_size=72).move_to(
            final_camera_center
        )
        self.play(Write(title), run_time=1.5)
        self.wait(0.5)

        self.play(
            title.animate.next_to(self.camera.frame.get_top(), DOWN, buff=0.7),
            run_time=1.5,
        )

        self._show_conclusion_algebra(final_camera_center)
        self._show_conclusion_geometry(final_camera_center)

    def _show_conclusion_algebra(self, camera_center):
        """Left half of the screen: Destino - Origen = (-Origen) + Destino."""
        left_position = camera_center + LEFT * 4

        destiny_minus_origin = MathTex(
            r"\text{Destino}", r"-\text{Origen}", font_size=60
        ).move_to(left_position)
        destiny_minus_origin[0].set_color(B_COLOR)
        destiny_minus_origin[1].set_color(A_COLOR)

        minus_origin_plus_destiny = MathTex(
            "(", r"-\text{Origen}", ")", "+", r"\text{Destino}", font_size=60
        ).move_to(left_position)
        minus_origin_plus_destiny[:3].set_color(A_COLOR)
        minus_origin_plus_destiny[4].set_color(B_COLOR)

        self.play(Write(destiny_minus_origin), run_time=1.5)
        self.wait(1.0)

        self.play(
            TransformMatchingTex(destiny_minus_origin, minus_origin_plus_destiny),
            run_time=1.5,
        )
        self.wait(1.0)

    def _show_conclusion_geometry(self, camera_center):
        """Right half of the screen: a vector with its angle and magnitude."""
        right_origin = camera_center + RIGHT * 4

        vector = Arrow(
            start=right_origin,
            end=right_origin + RIGHT * 2.5 + UP * 1.5,
            color=PURPLE_B,
            buff=0,
        )

        reference_line = DashedLine(
            vector.get_start(), vector.get_start() + RIGHT * 3.5, color=GRAY
        )
        angle = Angle(reference_line, vector, radius=1.2, color=ORANGE)
        angle_label = MathTex(r"\theta", font_size=40, color=ORANGE).next_to(
            angle, RIGHT, buff=0.2
        )
        magnitude_label = MathTex(r"||\vec{R}||", color=R_COLOR, font_size=40).next_to(
            vector.get_center(), UP * 0.2 + LEFT * 0.1
        )

        geometry_group = VGroup(
            vector, reference_line, angle, angle_label, magnitude_label
        )
        geometry_group.move_to(right_origin)

        self.play(GrowArrow(vector), Create(reference_line), run_time=1.5)
        self.play(
            Create(angle), Write(angle_label), Write(magnitude_label), run_time=1.5
        )
        self.wait(1.0)

        # Stretch & squash effect: the angle and labels follow the vector
        angle.add_updater(
            lambda m: m.become(Angle(reference_line, vector, radius=1.2, color=ORANGE))
        )
        angle_label.add_updater(lambda m: m.next_to(angle, RIGHT, buff=0.2))
        magnitude_label.add_updater(
            lambda m: m.next_to(vector.get_center(), UP * 0.2 + LEFT * 0.1)
        )

        # Rotate the vector and bring it back (changes the angle)
        self.play(
            Rotate(vector, angle=0.9, about_point=vector.get_start()),
            rate_func=there_and_back,
            run_time=1.5,
        )
        self.wait(0.3)

        # Scale the vector up and bring it back (changes the magnitude)
        self.play(
            vector.animate.scale(1.4, about_point=vector.get_start()),
            rate_func=there_and_back,
            run_time=1.5,
        )

        angle.clear_updaters()
        angle_label.clear_updaters()
        magnitude_label.clear_updaters()

        self.wait(3.0)

        self.wait(3.0)

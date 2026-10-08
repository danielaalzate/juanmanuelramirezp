---
name: Juan Manuel Ramírez Pérez
description: Warm editorial author website in blue ink with an orange alternative
colors:
  brand: "#233e52"
  brand-hover: "#172f41"
  hero-accent: "#b7d5e5"
  orange-brand: "#ad431b"
  orange-brand-hover: "#8b3313"
  orange-hero-accent: "#ffb975"
  cream: "#f6f2e9"
  ink: "#24221f"
  muted: "#625e55"
  rule: "#d1c8b8"
  on-brand: "#fffaf0"
typography:
  display:
    fontFamily: "Caslon, Georgia, serif"
    fontSize: "clamp(56px, 5.7vw, 88px)"
    fontWeight: 400
    lineHeight: 1.03
    letterSpacing: "-.025em"
  page-title:
    fontFamily: "Caslon, Georgia, serif"
    fontSize: "clamp(48px, 5.4vw, 86px)"
    fontWeight: 400
    lineHeight: 1.03
    letterSpacing: "-.025em"
  headline:
    fontFamily: "Caslon, Georgia, serif"
    fontSize: "clamp(38px, 4vw, 62px)"
    fontWeight: 400
    lineHeight: 1.03
    letterSpacing: "-.02em"
  title:
    fontFamily: "Caslon, Georgia, serif"
    fontSize: "29px"
    fontWeight: 400
    lineHeight: 1.03
  body:
    fontFamily: "Lato, Arial, sans-serif"
    fontSize: "17px"
    fontWeight: 400
    lineHeight: 1.65
  button:
    fontFamily: "Lato, Arial, sans-serif"
    fontSize: "15px"
    fontWeight: 700
rounded:
  control: "3px"
spacing:
  gutter: "clamp(22px, 4.1vw, 70px)"
components:
  button-primary:
    backgroundColor: "{colors.brand}"
    textColor: "{colors.on-brand}"
    rounded: "{rounded.control}"
    padding: "10px 23px"
    typography: "{typography.button}"
  button-primary-hover:
    backgroundColor: "{colors.brand-hover}"
    textColor: "{colors.on-brand}"
  button-outline:
    backgroundColor: "transparent"
    textColor: "{colors.brand}"
    rounded: "{rounded.control}"
    padding: "10px 23px"
---

# Design System: Juan Manuel Ramírez Pérez

## Overview

Approved warm editorial option A, adapted to blue ink with an interchangeable orange palette. Literary serif headings, warm cream surfaces and restrained rules frame the author's writing. Preserve this accepted direction.

The home page uses a wide study image and a blue shelf. The nine original covers provide the distinctive physical book treatment. No author study recording has been supplied: the hero currently identifies its generated image as illustrative and retains a configuration hook for a real video.

## Colors

Blue ink supplies navigation emphasis, action backgrounds, the book shelf and press section. The pale blue accent highlights the hero name. Orange swaps only brand, hover and hero accent; cream, ink, muted text, rules and warm light text remain shared.

The footer's “Color del sitio” controls select blue or orange. A valid `?tema=blue` or `?tema=orange` takes precedence over the saved `jmr-theme` preference and `SITE_CONFIG.defaultTheme`. Footer selections persist in local storage when available. Invalid theme values resolve to blue.

## Typography

The locally bundled Libre Caslon Display is registered as `Caslon`, with Georgia and serif fallbacks. Lato has local regular (400) and bold (700) faces, with Arial and sans-serif fallbacks. Both use `font-display: swap`.

The hero display reaches **88px**, while the general page title reaches 86px. Headings use normal weight, balanced wrapping and close line spacing. The hero subtitle is italic display type, `clamp(24px, 2.4vw, 37px)` with a 1.25 line height. Body text follows the frontmatter; biography paragraphs use a 1.8 line height and a maximum 68ch measure. Other text measures are contextual, such as 65ch for the author preview and 48ch for the subscription copy.

Book captions are 25px/1.15 on desktop; catalog titles are 33px/1.1. Navigation is 16px. Book metadata is uppercase 12px with .07em tracking; catalog category labels use .08em. These are component settings rather than a universal modular scale.

## Layout

The main container caps at 1600px and uses the fluid gutter in the frontmatter. The desktop header is 92px high. The hero has a 620px minimum and `height: min(690px, 75vw)`; at widths of at least 1650px it is 740px high. Home shelf, journal, author preview, biography and blog feature use asymmetric grids; catalog entries use three columns. Section spacing varies by component, commonly 38–80px.

At 1100px and below, gaps, navigation spacing, wordmark width and selected headings shrink. At 760px and below, the header becomes 78px high; its menu opens as a two-column panel. The shelf intro, journal, biography, blog and press content stack. Featured books remain three columns; the catalog becomes two columns. The author preview retains a compact image/text grid until 420px.

At 760px and below, the hero is 670px high, its crop moves to 66% center and the overlay emphasizes the bottom. Hero type becomes `clamp(48px, 9.5vw, 66px)`; page titles become 60px. Catalog book stages are 255px high with 205px book objects. At 420px and below, the hero is 650px, hero type is 51px, the author preview stacks, and catalog stages/books shrink to 215px/170px while retaining two columns. Journal images use the final 16:9 override at every breakpoint.

The HOME `.author-banner` uses a full-width cream surface with a two-column desktop composition: the original portrait on the left and the author's name in Caslon, reaching 88px, on the right, followed by his own biography and action. A bottom mask gradient, multiply blending and an edge fade integrate the portrait's original white background into the cream surface. Below 760px the banner stacks, with a 395px portrait and name type ranging from 45–64px. The composition draws on the supplied Pedro Salazar reference while retaining Juan Manuel Ramírez's content and the existing blue/orange palettes.

## Biography composition

The biography extends the home portrait treatment into a full editorial opening: the original `autor.png` portrait shares the home's cream blend, bottom mask and edge fade. A large Caslon statement, reaching 88px on desktop, introduces the author beside his name, profession, birthplace and birth date. The opening links into the trajectory, and a ruled section navigation provides anchors for formation, public life, writing and academies.

Formation and teaching use an asymmetric two-column chapter with a large serif lead and a separate teaching subsection. Culture and public life occupy a full-width brand-colored band, blue by default and orange when that palette is selected, with warm light text and two content columns. The writing chapter pairs the text with three original-cover book mockups—*Cuentos impertinentes*, *Huellas cifradas* and *Venezuela bajo el sol*—linked to their individual catalogue anchors. The academy block follows the same chapter alignment. A real photograph of the conversation with Federico Diazgranados closes the page with a link to the Blog encounters.

The biography preserves the sourced educational, teaching, diplomatic, institutional, literary and academy information; the redesign changes hierarchy and presentation without adding biographical claims. It reuses shared blue/orange tokens, book depth, keyboard focus and reduced-motion behavior. At 760px and below, the portrait and chapters stack, section navigation wraps, the opening heading becomes 54px, and the three selected books keep a compact three-column presentation. The encounter image uses a responsive crop while the Blog retains access to the complete photograph.

## Elevation & Depth

Layout surfaces are mostly flat, separated by color and fine rules. Book objects supply physical depth through 1100px perspective, a 23px spine, 22px page edge, a front translated 11px in depth and `14px 22px 21px -10px rgba(0,0,0,.28)` shadow. Spine and page inset shadows reinforce the construction. Original cover images are positioned using per-cover visible-bound variables; their text and artwork are not redrawn.

## Shapes

Buttons and palette controls use restrained 3px corners and 1px borders. Covers use `1px 3px 3px 1px` front corners. The interview play disc is circular (66px). Containers remain rectangular; separators are thin rules rather than floating rounded cards.

## Components

Primary buttons have a minimum 48px height, a brand background and warm light text. Hover deepens the brand; active applies .9 brightness. Outline buttons invert on hover, with contextual light outlines/text in the hero and press section. Background and color transitions last .2s. At 760px, buttons use 14px type and 17px horizontal padding, with additional compact hero/catalog overrides at 420px. Navigation, filters, synopsis summaries, theme controls and the video control have a minimum 44px height.

Navigation marks the current route with a brand-colored underline. Mobile navigation toggles `aria-expanded`, changes its accessible label and closes on Escape, returning focus to the menu button. A skip link appears on focus. Links, buttons and summaries have a 3px focus outline with a 5px offset; hero and shelf links use the light outline. Press links, hero buttons and interview play controls additionally use a light outline with an 8px brand-hover backing shadow for contrast.

Book links begin at `rotateY(-13deg) rotateZ(-1deg)`. Hover or keyboard focus changes to `rotateY(-4deg) rotateZ(0deg) translateY(-7px)` over .5s with `cubic-bezier(.16,1,.3,1)`. Reduced-motion removes transitions/animations, restores the resting book transform and changes smooth scrolling to automatic.

Catalog category buttons expose their selection with `aria-pressed`, hide nonmatching entries and update the publication count. Native details/summary elements reveal synopses. Eight original PDF links are present; Sonetos has no separate source PDF. Subscription access opens the original form.

The hero displays the labelled illustrative fallback until a configured real video plays. Only a configured source exposes the play/pause control. Reduced-motion prevents automatic playback and pauses an already playing video when the preference changes. The configured heroPoster updates both the image and video poster; heroPosterIllustrative determines whether the image is labelled illustrative or as the author in his study. Playback errors hide the failed video, restore the fallback notice and hide the control. The Nerdopolitan interview replaces its poster with a YouTube privacy-enhanced iframe only after activation.

## Do's and Don'ts

- Do preserve the approved warm editorial blue composition and interchangeable orange palette.
- Do keep original cover pixels and use CSS to construct book depth.
- Do retain clear download actions, visible keyboard focus and reduced-motion behavior.
- Don't describe the illustrative hero image as an actual author recording.
- Don't animate a still image to imply that real footage has been supplied.
- Don't invent missing publication facts, testimonials or download files.


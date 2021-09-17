use rand::Rng;

pub struct RGBA {
    pub r: u8,
    pub g: u8,
    pub b: u8,
    pub a: u8,
}

impl RGBA {
    fn new(r: u8, g: u8, b: u8, a: u8) -> RGBA {
        RGBA {
            r: r,
            g: g,
            b: b,
            a: a,
        }
    }

    fn random() -> RGBA {
        RGBA {
            r: RGBA::random_color(),
            g: RGBA::random_color(),
            b: RGBA::random_color(),
            a: RGBA::random_alpha(),
        }
    }

    fn random_color() -> u8 {
        let mut rng = rand::thread_rng();

        rng.gen_range(0..255)
    }

    fn random_alpha() -> u8 {
        let mut rng = rand::thread_rng();

        rng.gen_range(30..60)
    }

    fn mutate_red(&mut self) {
        self.r = RGBA::random_color()
    }

    fn mutate_green(&mut self) {
        self.g = RGBA::random_color()
    }

    fn mutate_blue(&mut self) {
        self.r = RGBA::random_color()
    }

    fn mutate_alpha(&mut self) {
        self.a = RGBA::random_color()
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_new() {
        let r: u8 = 12;
        let g: u8 = 84;
        let b: u8 = 120;
        let a: u8 = 22;
        let c = RGBA::new(r, g, b, a);

        assert_eq!(c.r, r);
        assert_eq!(c.g, g);
        assert_eq!(c.b, b);
        assert_eq!(c.a, a);
    }
}

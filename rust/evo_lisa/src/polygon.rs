use rand::Rng;

use crate::point::Point;

pub struct Polygon {
    pub origin: Point,
    pub y: u16,
}

// impl Point {
//     fn new(x: u16, y: u16) -> Point {
//         Point { x: x, y: y }
//     }

//     fn random(max_x: u16, max_y: u16) -> Point {
//         let mut rng = rand::thread_rng();

//         Point {
//             x: rng.gen_range(0..max_x),
//             y: rng.gen_range(0..max_y),
//         }
//     }
// }

// #[cfg(test)]
// mod tests {
//     use super::*;

//     #[test]
//     fn test_new() {
//         let x: u16 = 12;
//         let y: u16 = 84;
//         let p = Point::new(x, y);

//         assert_eq!(p.x, x);
//         assert_eq!(p.y, y);
//     }
// }

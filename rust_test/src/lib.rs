use std::f64;

#[no_mangle]
pub extern "C" fn fast_function() -> f64 {
    let mut total: f64 = 0.0;
    for i in 1..10_000_000 {
        total += (i as f64).sqrt(); // Kvadrat ildizni hisoblash
    }
    total
}

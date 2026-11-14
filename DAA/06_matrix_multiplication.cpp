#include <iostream>
#include <stdexcept>
#include <vector>
#include <windows.h>

using Matrix = std::vector<std::vector<int>>;

struct ThreadContext {
    const Matrix* a;
    const Matrix* b;
    Matrix* result;
    size_t row;
};

DWORD WINAPI multiplyRow(LPVOID parameter) {
    auto* context = static_cast<ThreadContext*>(parameter);
    for (size_t col = 0; col < context->b->at(0).size(); ++col)
        for (size_t k = 0; k < context->b->size(); ++k)
            context->result->at(context->row).at(col) += context->a->at(context->row).at(k) * context->b->at(k).at(col);
    return 0;
}

Matrix multiply(const Matrix& a, const Matrix& b) {
    if (a.empty() || b.empty() || a[0].size() != b.size())
        throw std::invalid_argument("incompatible matrix dimensions");
    Matrix result(a.size(), std::vector<int>(b[0].size()));
    std::vector<ThreadContext> contexts;
    std::vector<HANDLE> workers;
    contexts.reserve(a.size());
    for (size_t row = 0; row < a.size(); ++row) {
        contexts.push_back({&a, &b, &result, row});
        workers.push_back(CreateThread(nullptr, 0, multiplyRow, &contexts.back(), 0, nullptr));
    }
    WaitForMultipleObjects(static_cast<DWORD>(workers.size()), workers.data(), TRUE, INFINITE);
    for (HANDLE worker : workers) CloseHandle(worker);
    return result;
}

int main() {
    Matrix a{{1, 2}, {3, 4}}, b{{5, 6}, {7, 8}};
    for (const auto& row : multiply(a, b)) {
        for (int value : row) std::cout << value << ' ';
        std::cout << '\n';
    }
}
